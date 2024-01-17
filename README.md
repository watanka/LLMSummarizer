

## 기능 정의
인풋 : 유튜브 url과 OpenAI api키
아웃풋 : 요약본

![](img/llmsummarizer-pipeline.png)

## 기록
- [LLMSummarizer 프로젝트(1) - 왜 나는 같은 프로젝트를 다시 진행하게 되었을까?](https://watanka.github.io/blog/posts/LLMSummarizer%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B81/)
- [LLMSummarizer 프로젝트(2) CI/CD 구성](https://watanka.github.io/blog/posts/LLMSummarizer%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B82/)


## 개선 포인트
[ ] pytube는 borg 패턴으로 pytube.streams.Stream 클래스를 리턴. audio 파일 핸들링
- 파일과 stream의 차이? 메모리에 있는 데이터와 파일에 있는 데이터와 어떻게 다른건지?