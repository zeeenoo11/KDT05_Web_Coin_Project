from flask import Blueprint, render_template, request, redirect, url_for
from CoinWeb import db
from CoinWeb.model import BTCUSDT_1d, Treasury20Y, Vix, WtiOilPrice, HistCoin
from CoinWeb import predictor


# --------------------------------------------------------------------------------
# 문섭님 블루프린트 코드
# bp = ms_bp, url_prefix = '/kms'
# --------------------------------------------------------------------------------
ms_bp = Blueprint('ms_main_views', __name__, url_prefix='/kms')

whattopredict = {
    'vix': 1,
    'treasury': 2,
    'oil': 3,
}

@ms_bp.route('/')
def home():
    print(predictor.data.shape)
    result = BTCUSDT_1d.query.order_by(BTCUSDT_1d.timestamp.desc()).limit(100).all()
    predict = BTCUSDT_1d.query.order_by(BTCUSDT_1d.timestamp.desc()).limit(30).all()
    result.reverse()
    predict.reverse()
    return render_template('kmsindex.html', result=result, predict = predict)

@ms_bp.route('/predict', methods = ['POST'])
def predict():
    forms = request.form
    result = None
    bitresult = BTCUSDT_1d.query.order_by(BTCUSDT_1d.timestamp.desc()).limit(100).all()
    bitresult.reverse()
    if forms['symbol'] == 'vix':
        target = 'VIX'
        result = Vix.query.order_by(Vix.date.desc()).limit(100).all()
        predict = predictor.result_vix()
        result.reverse()
        return render_template('result_date.html', result=result, predict=predict, target=target, bitresult = bitresult)
    if forms['symbol'] == 'coin':
        target = '코인베이스'
        result = HistCoin.query.order_by(HistCoin.date.desc()).limit(100).all()
        predict = predictor.result_coin()
        result.reverse()
        return render_template('result_date.html', result=result, predict=predict, target=target, bitresult = bitresult)
    if forms['symbol'] == 'oil':
        target = 'WTI 오일 가격'
        result = WtiOilPrice.query.order_by(WtiOilPrice.DATE.desc()).limit(100).all()
        predict = predictor.result_oil()
        result.reverse()
        return render_template('result_DATE_oil.html', result=result, predict=predict, target=target, bitresult = bitresult)

    return render_template('kmsindex.html', result=result, predict=predict)
    