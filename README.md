# Module_Team_Project

recommend_stock.py -> 주식 종목 추천</br>
get_stock_info.py -> 종목별 재무제표 csv파일로 저장</br>
extract_code200.py -> 코스피200 종목 코드 추출

stock_num.csv -> 코스피200 종목 번호</br>
stock_code_200.csv -> 재무제표 데이터 (원본)</br>
financial_statement.csv -> 재무제표 + 데이터 처리</br>

# Team

김재원 진하영 정승철 한지혜


# 팀 프로젝트 주제

## 데이터 소스

    1. 주식 (5분 or 15 분 ...)
        - https://finance.naver.com/main/main.nhn

## 데이터 수집
    - 크롤링 (Crawling) Scrapy
    - Pipeline -> kafka -> RDS

## 데이터 저장
    - zookeeper + Kafka
    - kafka connect (source, sink)
    - kafka Broker...

## 데이터 분석 
    - Python data analysis (pandas, Numpy, Matplotlib)
    - 기본적인 기술 통계
    - 시각화... 

## 시스템 운영
    - Public cloud
    - Docker container (X)

# 구현 과정

    1. 주제 선정(주식 데이터 실시간 처리)
    2. 기능 선정()
        a) 코스피 200종목 추출
        
        b) 주식거래량 TOP5
        
        c) 종목 추천
            - 현재 추세 + 재무제표 현황

        d) 종목 세부 데이터 출력
        
    3. API 설계 - 입력 주소, 입력 파라미터, 출력 파라미터, 출력 데이터
    
        a) 코스피 200종목 데이터
        -  (GET) http://3.130.233.168:8000/my_stock_table/
        
        b) 주식 거래량 TOP 5
        -  (GET) http://3.130.233.168:8000/my_stock_table/trade_rank

        c) 종목 추천
        - (GET) http://3.130.233.168:8000/my_stock_table/recommend_stock

        d) 세부 데이터
        - (GET) http://3.130.233.168:8000/my_stock_table/inf0_detail/?code=009410
    
    4. Infrastructure 구성
    5. Scrapy 구현
    6. Kafka 구성
    7. RDS 구성
    8. Python + Django + RESTful API 구성
        - Djanggo(학습 전)
        - Rest framework(학습 전)
    9. 보고서 제출
    
# 세부 내용
1. 1개의 테이블 200개의 종목 넣어보기
    - 테이블이 존재하지 않으면 생성
    - 있다면 데이터 추가

    a) 이전 데이터 가져오기<br/>
    b) 실시간 데이터 가져오기

2. 재무제표 분석 -> 회사 실적 평가

3. 주식 최근동향 분석

4. 종목 추천
5. 거래 가장 활발한 종목 5
