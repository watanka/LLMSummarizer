

## 기능 정의
인풋 : 유튜브 url, openai api key
아웃풋 : 요약본



## 필요한 기능
- 인풋 검증 - 유효한 유튜브 url인지
- openai api key 검증
- url -> transcription
- transcription -> url


- pytube는 borg 패턴으로 pytube.streams.Stream 클래스를 리턴
- audio 파일 핸들링
- 파일과 stream의 차이? 메모리에 있는 데이터와 파일에 있는 데이터와 어떻게 다른건지?