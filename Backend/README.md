# 설치 및 실행 가이드

## 1. 필수 패키지 설치

프로젝트에 필요한 패키지는 `requirements.txt` 파일에 정의되어 있습니다. 아래 명령어를 사용해 패키지를 설치하세요
```
pip install ./requirements.txt
```

주요 패키지:
- fastapi: 웹프레임워크
- uvicorn: ASGI 서버
- motor: 비동기 MongoDB 드라이버
- pytest: 테스트 프레임워크

## 2. 데이터베이스 실행

FastAPI 웹 애플리케이션을 실행하기 전, 데이터베이스를 실행해야합니다.

```bash
docker compose up -d
```

웹브라우저에서 `http://localhost:8081` 주소로 접속 후, `admin:pass`로 MongoDB를 관리할 수 있습니다.

## 2. 웹서버 실행

FastAPI 웹 애플리케이션을 실행하려면 아래 방법 중 하나를 선택하세요

**방법 1. 직접 실행**

```
python -m app.main
```

**방법 2. 스크립트 실행**

```
./run.sh
```

웹서버가 실행되면 웹브라우저에서 `http://localhost:8000` 주소로 접속하세요

- Swagger UI (API 문서 및 테스트): `http://localhost:8000/docs`

- ReDoc (대체 API 문서): `http://localhost:8000/redoc`

## 3. Python 환경

이 프로젝트는 **Python 3.11.5** 버전에서 개발되었습니다.


# 테스트 실행

**0. 테스트 환경**

테스트 도구: pytest, pytest-asyncio

**1. 모든 테스트 실행**

모든 테스트를 실행하려면 아래 명령어를 사용하세요

```
pytest
```

**2. 특정 파일 실행**

특정 테스트 파일만 실행하려면 아래와 같이 파일 경로를 지정해야 합니다.

```
pytest .\tests\test_example_api.py
```

**3. 상세 출력**

테스트 결과를 더 자세히 확인하려면 `-v` 옵션을 추가합니다.
```
pytest -v
```