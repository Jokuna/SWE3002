# 설치 및 실행가이드

1. Node.js

이 프로젝트는 Node.js 20.12.2으로 개발되었습니다.

2. 필수 패키지 설치

프로젝트를 실행을 위해 필요한 패키지를 설치합니다.

```bash
npm i
```

3. 개발 서버 열기

아래 명령어를 사용하여 개발 서버를 실행합니다.

```bash 
npm run dev
```

실행 후 웹브라우저에서 http://localhost:3000/에 접속하여 개발 중인 웹 애플리케이션을 확인할 수 있습니다.

## 배포방법

1. Build 생성

애플리케이션을 배포할 수 있도록 빌드를 생성합니다.

```bash
npm run build
```

2. node로 실행

빌드된 파일을 Node.js를 이용해 실행합니다.

```bash
node ./.output/server/index.mjs
```

3. 애플리케이션 확인

웹브라우저에서 http://localhost:3000/에 접속해 배포된 애플리케이션을 확인합니다.
