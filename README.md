# project_musinsa_crawling
- 팀 멋쟁이 무신사 크롤러

---
# 임시 README

## 0. 설계도

- 1. 크롤러 (MUSINSA 웹 사이트 상품 이미지, 상품 정보 크롤러)
- 2. AI hub Data를 활용하여 이미지 라벨링(모델 or 상품 이미지) 모델 구축 
- 3. 이를 활용하여 크롤링 된 데이터 자동 라벨링
- 4. 이후 라벨링 데이터를 활용하여 라벨링 모델 추가 학습 및 추가 크롤링 

## 1. 추가 
- 1. Poetry를 활용하여 버전 관리

> Windo Poetry 설지
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

> Linux, macOS, Windows (WSL) 설치
```
curl -sSL https://install.python-poetry.org | python3 -
```

> `poetry --version`으로 설치 확인, 만약 찾지 못한다면 `환경변수` 지정해주어야함  
- 관련 링크 : [링크](https://velog.io/@liso_o/Poetry-%ED%99%98%EA%B2%BD-%EB%B3%80%EC%88%98-%EC%84%A4%EC%A0%95)
