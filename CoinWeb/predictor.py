from sqlalchemy import create_engine, Connection, text
from sklearn.impute import KNNImputer
import pandas as pd
import holidays
from pytorch_forecasting import Baseline, TemporalFusionTransformer, TimeSeriesDataSet

engine = create_engine('mysql+pymysql://root:kdt5@1.251.203.204:33065/Team2?charset=utf8mb4')

with engine.begin() as conn:
    data = pd.read_sql(text('SELECT * FROM BTCUSDT_1d_latest'), conn)
    vix = pd.read_sql(text('SELECT * FROM vix'), conn)
    t20y = pd.read_sql(text('SELECT * FROM treasury_20y'), conn)
    oil = pd.read_sql(text('SELECT * FROM wti_oil_price'), conn)
    coinbase = pd.read_sql(text('SELECT * FROM hist_coin'), conn)

COINBASE = False

data = pd.merge(data, vix, left_on='timestamp', right_on='date', how='left', suffixes=('', '_vix'))
data = pd.merge(data, t20y, left_on='timestamp', right_on='Date', how='left', suffixes=('', '_t20y'))
data = pd.merge(data, oil, left_on='timestamp', right_on='DATE', how='left', suffixes=('', '_oil'))
data_coinbase = pd.merge(data, coinbase, left_on='timestamp', right_on='date', how='left' , suffixes=('', '_coinbase'))

def preprocess(data):
    data['time_idx'] = data.index
    data['time_idx'] -= data['time_idx'].min()
    data['pairs'] = 'BTCUSDT'
    data['diff'] = (data['close']-data['open']).div(data['open'])
    data['diff_vix'] = (data['close_vix']-data['open_vix']).div(data['open_vix'])



    data.interpolate(method='linear', inplace=True)
    data.dropna(inplace=True, axis=0)
    return data



data_coin = preprocess(data_coinbase)
data_coin['diff_coinbase'] = (data_coin['close_coinbase'] - data_coin['open_coinbase']).div(data_coin['open_coinbase'])
print(data_coin.columns)
data = preprocess(data)


en_holidays = holidays.UnitedStates()
cn_holidays = holidays.China()
holidf = pd.DataFrame(columns=['date', 'isholiday'])
holidf['date'] = data['timestamp']
holidf['isholiday'] = holidf['date'].apply(lambda x: 'yes' if x in en_holidays or x in cn_holidays else 'no')
holidf['isholiday'].value_counts()

data['isholiday'] = holidf['isholiday']
data_coin['isholiday'] = holidf['isholiday']

data['month'] = data.timestamp.dt.month.astype(str).astype('category')
data_coin['month'] = data_coin.timestamp.dt.month.astype(str).astype('category')


max_prediction_length = 3
max_encoder_length = 7

def model_result(path, data):
    best_model_path = path
    best_tft = TemporalFusionTransformer.load_from_checkpoint(best_model_path)
    predict = best_tft.predict(data[0], return_x = True ,return_y=True, mode='raw', trainer_kwargs = dict(accelerator="cpu"))
    df = pd.DataFrame(list(predict.output.prediction.numpy()[0]), columns=[str(x) for x in [0.02, 0.1, 0.25, 0.5, 0.75, 0.9, 0.98]])
    dfdate = pd.DataFrame([[x] for x in data[1].iloc[-max_prediction_length:].tolist()], columns=['timestamp'])
    df = pd.concat([dfdate, df], axis=1)
    return df

def result_coin():
    best_model_path = 'models_kms/coin.ckpt'
    padded_data = prepare_data(data_coin, max_prediction_length, max_encoder_length)
    result = model_result(best_model_path, padded_data)
    return result

def result_vix():
    best_model_path = 'models_kms/vix.ckpt'
    padded_data = prepare_data(data_coin, max_prediction_length, max_encoder_length)
    result = model_result(best_model_path, padded_data)
    return result

def result_oil():
    best_model_path = 'models_kms/oil.ckpt'
    padded_data = prepare_data(data_coin, max_prediction_length, max_encoder_length)
    result = model_result(best_model_path, padded_data)
    return result



def prepare_data(data, max_prediction_length, max_encoder_length):
    from datetime import timedelta
    
    encoder_data = data[lambda x: x.time_idx > (x.time_idx.max() - max_encoder_length)]
    last_data = data[lambda x: x.time_idx == x.time_idx.max()]
    decoder_data = pd.concat(
        [last_data.copy().assign(timestamp = lambda x: x['timestamp'] + timedelta(days=i)).assign(time_idx = lambda x : x['time_idx'] + i) for i in range(1, max_prediction_length + 1)],
        ignore_index=True,
    )

    decoder_data["month"] = decoder_data.timestamp.dt.month.astype(str).astype("category")
    new_prediction_data = pd.concat([encoder_data, decoder_data], ignore_index=True)
    print(new_prediction_data)
    return new_prediction_data, decoder_data['timestamp']

    