# project_musinsa_crawling
- 팀 멋쟁이 무신사 크롤러

---
## Tree
```
project_musinsa_crawling
┣ README.md
┣ .gitignore
┣ save : save csv and img
┣ musinsa-crawling
┃┣ main.py : crawling code example
┃┣ musinsa : crawler package - source code
┃┃ ┣ __init__.py
┃┃ ┣ crawler.py
┃┃ ┗ utils.py
┃┣ poetry.lock
┃┣ pyproject.toml
┃┗ README.md
```

## 1. Ues Poetry
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

## 2. requirements
`poetry.lock`와 `pyroject.toml` 참고

```
python = "^3.9"
beautifulsoup4 = "^4.12.2"
requests = "^2.31.0"
selenium = "^4.10.0"
pandas = "^2.0.2"
torch = "^2.0.1"
lxml = "^4.9.2"
urllib3 = "^2.0.3"
tqdm = "^4.65.0"
```

- `poetry.lock`파일로부터 requirements.txt생성
```
poetry export -f requirements.txt > requirements.txt
```

- 해당 패키지들 설치 방법
`pyproject.toml` 파일이 있는 경로에서 아래 명령어 실행
```
poetry install
```

## 3. 사용법
- `./musinsa-crawling` 디렉토리로 이동
```
cd musinsa-crawling
```

- `poetry shell` 활성화 하기
```
poetry shell
```

- `main.py` 실행 
```
python main.py {argsparser}
```

- `argsparser` 세부내용
```
--save_path : csv, img 저장 경로 (defalut : ../save)
--category : crawling할 상품 카테고리
--crawling_num : crawling할 데이터 수
```
---

## 4. 지원되는 상품 카테고리
```

'Top': '001',
'Outer': '002',
'Pants': '003',
'Onepiece': '020',
'Skirt': '022'

```

- 추가하고 싶은 상품 카테고리는 ./musinsa/utils.py/setting_url의 `url_dict`에 dict 형태로 추가해주면 됩니다 (**추후 추가해주는 메소드 구현 예정**) 

