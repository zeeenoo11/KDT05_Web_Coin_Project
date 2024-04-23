# Bitcoin Analysis Project

## Introduction

### Background

#### 1. 활용 목표

: 이번 주 수업의 주제는 웹 활용으로, 이번 주차에 배운 html상의 데이터 송수신과 DB 활용을 목표로 한다.

#### 2. 주제

: 지난 프로젝트에서 활용한 RNN 시계열 분석에 이어, 다양한 외부 변수를 고려한 비트코인 가격 예측 모델을 구축한다.

#### 3. 목표 및 방법

1. 비트코인 가격 예측 모델 구축
2. 외부 변수 탐색 및 반영
3. 정확도 향상을 위한 다양한 시도
4. 최종 모델 선정 및 예측
5. 결과 시각화 및 해석
6. 웹페이지 구축
7. DB 연동 필요

### Data

- 바이낸스 크롤링 : 문섭님
- 외부 변수 : 달러 가치, 금값, 나스닥
- 뉴스와 sns 등을 활요하면 좋겠지만 패스

### Method

- RNN
- Transformer

## 1. Data Collection

### 외부 변수 1 : 달러 가치

https://www.tossbank.com/articles/23697 : 달러 가치에 대한 설명

![alt text](image.png)
![alt text](image-1.png)

- 출처 : 토스뱅크

- 달러 인덱스 : 주요 6개 통화에 대한 달러 가치를 나타내는 지표
- 세계적인 경제 상황을 파악하는데 중요한 지표

#### 달러 인덱스 기준 : 1973년 3월 - 100으로 기준

![alt text](image-2.png)
![alt text](image-3.png)

#### 영향 - 환율, 금리, 수입수출품 가격

- 환율 : 달러 인덱스 상승 -> 원화 가치 하락
- 금리 : 달러 인덱스 상승 -> 미국 금리 상승
- 수입수출품 가격 : 달러 인덱스 상승 -> 수입품 가격 상승

> 데이터 출처 : https://kr.investing.com/

- DXY : 달러 인덱스 지표
- 데이터 () : 2005/04/20 ~ 2024/04/19
- 데이터 (2) : 1986/04/21 ~ 2005/04/19
- 데이터 (3) : 1979/12/26 ~ 1986/04/18

- pandas로 하나로 모으기

### 외부 변수 2 : 금값

- 금 가격의 세계적 지표 : GCM4
- 데이터 출처 : https://kr.investing.com/
- 데이터 기간은 위 날짜와 동일 (3 파일)

### 외부 변수 3 : S&P 500

- 데이터 출처 : https://kr.investing.com/

미국 대표 주가지수 : 다우존스, S&P 500, 나스닥

- 다우존스 : 총 30개 기업, 산업주 중심 (예: Boeing, Coca-Cola, IBM, McDonald's, Microsoft 등)

- 나스닥 : 총 100개 기업, 기술주 중심 (예: Apple, Amazon, Facebook, Google, Microsoft 등)

- S&P 500 : 총 500개 기업, 다우존스보다 넓은 범위 (예: Apple, Amazon, Facebook, Google, Microsoft 등)
  - 전체 주식 시장의 80%를 대표

![alt text](image-4.png)
: 출처 - KB증권

- S&P 500이 더 포괄적이기 때문에 S&P 500을 활용

- 데이터 기간은 위 날짜와 동일 (3 파일)
- 데이터 (1) (2) (3)

## 4월 20일 : 토요일 작업

### 할 일

[ㅇ] 데이터 다듬기 - 통합 (난중하 우상)
[ㅇ] 데이터 가져오기 - 비트코인 (난상 우상)
[] 데이터 모아서 시각화 - 인사이트 도출 (난중 우상)
[] pytorch forecast 공부 (난상 우상)
[] html 프레임 짜기 (난중 우상)
[] DB 연동 (난최상 우중)

개인적으로 할 일
[] 리빙랩 영수증 (코파일럿) 제작 (난중하 우상)
[] 학교 연락할 내용 정하기 (난하 우중)

### 1. 데이터 편집 : 통합하기

[01_data_preprocessing.ipynb](../01_data_preprocessing.ipynb)

![alt text](image-5.png)  
: Gold, Dollar, S&P 500 데이터 지표 : Gold가 왜 안보이지?

![alt text](image-7.png)  
: dollar에 gold 데이터를 넣었다...

- 데이터간 범위가 너무 상이해 표준화 필요

- 가격 변동을 보기 위해 표준화
  결측치 채우기
- 방법 : 평균, 중앙값, 직전값, 직후값, 보간법
- 보간법 : 선형, 다항식, 시계열
- 시계열 보간법 : 시계열 데이터의 특성을 고려하여 결측치를 채워넣는 방법

![alt text](image-6.png)  
: .interpolate() : 시계열 데이터의 결측치를 보간하는 함수 - 비교

- 잘 나오는 것을 알 수 있다

![alt text](image-8.png)

![alt text](image-9.png)  
: 표준화가 잘 진행 되었다

- 저장 > DATA

### 2. 데이터 시각화 : 시계열 -> 우선 db 연동해 데이터 받기
> 접근 완료! [02_connect_sql.ipynb](../02_connect_sql.ipynb)

- 데이터베이스 연동 : MySQL
- 방법 : pymysql, sqlalchemy
- pymysql : MySQL DB와 연동하기 위한 라이브러리
- sqlalchemy : ORM(Object Relational Mapping)을 지원하는 라이브러리

![alt text](image-10.png)  
![alt text](image-11.png)  
: DB에 데이터 올리기. 신기하다...
![alt text](image-12.png)  
: 디게 오래 걸린다
![alt text](image-13.png)  
: 끝!

- 데이터 불러오기 : BTCUSDT_1d
> [03_load_data.ipynb](../03_load_data.ipynb)

성공!

### 3. 시각화
[04_visual_prepare.ipynb](../04_visual_prepare.ipynb)

1. 데이터 불러오기 : BTCUSDT_1d, Gold, Dollar, S&P 500
2. 데이터 합치기

[05_visual.ipynb](../05_visual.ipynb)  
: ㅎ 여기서 새로 scaling해서 다시 파일 만듦

[06_visualize.ipynb](../06_visualize.ipynb)  

![alt text](image-14.png)  
: 그냥 보면 잘 모르겠다

## 4월 21일 : 일요일 작업

### 할 일
[] pytorch forecast 공부 (난상 우상)
[] html 프레임 짜기 (난중 우상)
[] 데이터 모아서 시각화 - 인사이트 도출 (난중 우중)
[] DB 연동 (난최상 우중)

개인적으로 할 일
[] 리빙랩 영수증 (코파일럿) 제작 (난중하 우상)
[] 학교 연락할 내용 정하기 (난하 우중)

### 예측 관련 자료

#### 예측
이란 주어진 이용가능한 모든 정보(과거 데이터 및 예측에 영향을 끼칠 수 있는 미래 사건에 대한 지식을 포함)를 바탕으로 가능한 한 정확하게 미래를 예측하는 것입니다.
#### 목표
는 예측 및 계획과 연관되어 있는 것이 좋지만, 이것이 항상 일어나는 것은 아닙니다. 목표를 어떻게 달성할지에 대한 계획과 목표가 실현 가능한지에 대한 예측 없이 목표를 세우는 경우가 너무나도 자주 있습니다.
#### 계획
은 예측과 목표에 대한 대응입니다. 계획은 여러분의 예측과 목표를 일치시키는데 필요한 적절한 행동을 결정하는 일을 포함합니다.  
회사의 많은 영역에서 중요한 역할을 할 수 있기 때문에, 예측은 경영에서 의사결정 행동에 있어서 중요한 요소가 되어야합니다. 현대 기업들은 특정한 용도에 따라 단기, 중기, 장기 예측을 필요로 하고 있습니다.

#### 단기 예측
은 인사, 생산, 수송 계획 등에 필요합니다. 계획 과정의 한 부분으로 수요 예측도 필요합니다.
#### 중기 예측
은 원자재 구입, 신규 채용, 장비나 기계 구입 등 미래 자원 공급을 결정하는데 필요합니다.
#### 장기 예측
은 전략적으로 계획을 세우는데 사용합니다. 시장 기회, 환경 요인, 내부 자원을 반드시 고려하여 결정합니다.

### 1. forecasting

[07_forecasting_test.ipynb](../07_forecasting_test.ipynb)

- doc를 읽고 forecasting을 해보자
- prophet, ARIMA, LSTM, GRU, Transformer
- prophet : Facebook에서 개발한 시계열 예측 라이브러리
- ARIMA : AutoRegressive Integrated Moving Average
- LSTM : Long Short-Term Memory
- GRU : Gated Recurrent Unit
- Transformer : Attention is All You Need

![alt text](image-15.png)  
: 모델의 종류

- 여기에 MinMaxScaler가 있었다,,