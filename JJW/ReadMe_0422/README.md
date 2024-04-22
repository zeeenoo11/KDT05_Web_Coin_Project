# 4월 21일 : 일요일 작업

## 할 일

[ㅇ] pytorch forecast 공부 (난상 우상)  
[ㅇ] forecast 작성 (난최상 우상)  
[ㅇ] 결과 분석 (난중 우상)  
[] html 프레임 짜기 (난중 우상)  
[] 값 변경-학습 기간 늘리기 (난중 우중)  
[ㅇ] 데이터 모아서 시각화 - 인사이트 도출 (난중 우중)  
[] DB 연동 (난최상 우중)

개인적으로 할 일
[] 리빙랩 영수증 (코파일럿) 제작 (난중하 우상)  
[] 학교 연락할 내용 정하기 (난하 우중)  

### 예측 관련 자료

#### 예측

이란 주어진 이용가능한 모든 정보(과거 데이터 및 예측에 영향을 끼칠 수 있는 미래 사건에 대한 지식을 포함)를 바탕으로 가능한 한 정확하게 미래를 예측하는 것입니다.  
내 예측 : 비트코인의 가격 예측

#### 목표

는 예측 및 계획과 연관되어 있는 것이 좋지만, 이것이 항상 일어나는 것은 아닙니다. 목표를 어떻게 달성할지에 대한 계획과 목표가 실현 가능한지에 대한 예측 없이 목표를 세우는 경우가 너무나도 자주 있습니다.  
목표 : 높은 정확도로 예측

#### 계획

은 예측과 목표에 대한 대응입니다. 계획은 여러분의 예측과 목표를 일치시키는데 필요한 적절한 행동을 결정하는 일을 포함합니다.  
계획 : 상승한다면 구매, 하락한다면 판매

회사의 많은 영역에서 중요한 역할을 할 수 있기 때문에, 예측은 경영에서 의사결정 행동에 있어서 중요한 요소가 되어야합니다. 현대 기업들은 특정한 용도에 따라 단기, 중기, 장기 예측을 필요로 하고 있습니다.  
중장기 요소 : 계절성(반감기), 경기변동(유가와 금리)

## 1. forecasting

- doc를 읽고 forecasting을 해보자
- prophet, ARIMA, LSTM, GRU, Transformer
- prophet : Facebook에서 개발한 시계열 예측 라이브러리
- ARIMA : AutoRegressive Integrated Moving Average
- LSTM : Long Short-Term Memory
- GRU : Gated Recurrent Unit
- Transformer : Attention is All You Need
- 여기에 MinMaxScaler가 있었다,,

![alt text](image-15.png)  
: 모델의 종류

## 2. 모델 선택하기

: 그전에 이해가 필요

### 1) Availability of Covariates

- 공변량의 유무
- 공변량 : 예측에 영향을 미치는 변수
- 공변량이 없으면 ARIMA, prophet
- 공변량이 있으면 LSTM, GRU, Transformer

### 2) Length of Time Series

- 시계열의 길이
- 시계열이 짧으면 TemporalFusionTransformer
- 단기 예측에 특화
- cold-start prediction : 새로운 시계열 데이터에 대한 예측

### Type of prediction task : 예측 작업 유형

Not every can do regression, classification or handle multiple targets. Some are exclusively geared towards a single task. For example, **NBeats** can only be used for regression on a single target without covariates while the **TemporalFusionTransformer** supports multiple targets and even hetrogeneous targets where some are continuous variables and others categorical, i.e. regression and classification at the same time. **DeepAR** can handle multiple targets but only works for regression tasks.  
For long forecast horizon forecasts, **NHiTS** is an excellent choice as it uses interpolation capabilities.

> NBits : 단일 대상 회귀
> TemporalFusionTransformer : 다중 대상, 회귀 및 분류

> 다중대상(공변량), 회귀 -> TemporalFusionTransformer

## 3. TemporalFusionTransformer

[07_forecasting_test.ipynb](../07_forecasting_test.ipynb)

### 겨우겨우 제작 완료

: 왜 크게 차이나지...

### 발표용 그래프

![alt text](image-7.png)

![alt text](image-2.png)  

![alt text](image-8.png)
: 수정한 그래프 : 날짜 수정


![alt text](image-3.png)

![alt text](image-4.png)

![alt text](image-5.png)

![alt text](image-6.png)

> Encoder 변수 중요도에서 월이 가장 중요하고, 금값이 다음이다.

## 4. 미래 데이터 예측

해당 페이지임 (07_)

### 데이터를 변환시켜주는 게 어려웠다
- 날짜를 바꿔 입력해야함

![alt text](image-9.png)  
: 3-31이 마지막 데이터  

## 중간 정리

1. forecast 를 공부했고
2. temporalFusionTransformer를 선택했고
3. 예시에 적용해보았다
4. 결과를 분석하고 저장했으며
5. 날짜 인덱스 변경 및 결과값 출력법을 익혔다

## 5. html 프레임 짜기
: 이제 html을 만들어보자

### 만들어야 하는 것
: flask, sqlalchemy를 이용
1. jw_input.html
2. result.html
3. jw_pred.py

### 구성
: 일단 NooWeb을 복사해서 옴

## 다음에 할 일

1. html 프레임 짜기
2. 결과값을 출력하고 이를 표현하는 방법 찾기 (chart.js)
3. 값 변경-학습 기간 늘리기


![](image-10.png)  
: 이걸 어떻게 이해한거여... 
