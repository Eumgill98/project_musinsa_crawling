# Musinsa Crawling 

```
musinsa-crawling
┣ save
┣ src_
┃ ┣ crawling.py
┃ ┗ utils.py
┣ poetry.lock
┣ pyproject.toml
┗ README.md
```

## 01. 사용법
- `musinsa-crawling` 디렉토리로 이동
```
cd musinsa-crawling
```

- `poetry shell` 활성화 하기
```
poetry shell
```

- `src` 폴더로 이동
```
cd src
```

- `crawling.py` 실행 
```
python crawling.py {argsparser}
```

- `argsparser` 세부내용
```
--save_path : csv, img 저장 경로 (defalut : ../save)
--category : crawling할 상품 카테고리
--crawling_num : crawling할 데이터 수
```

---

## 02. requirements
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
progressbar = "^2.5"
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

