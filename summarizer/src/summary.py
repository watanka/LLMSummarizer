from summarizer.src.inputhandler import AbstractInputHandler, YoutubeInputHandler
from summarizer.src.transcriber import AbstractTransriber, WhisperAPITranscriber
from summarizer.src.mapreducer import AbstractMapReducer, LangChainMapReducer


def summarize(
    url,
    api_key,
    input_handler: AbstractInputHandler,
    transcriber: AbstractTransriber,
    mapreducer: AbstractMapReducer,
):
    # parser 정의. pytube 사용
    input_handler.parse(url)

    # url이 유효한 youtube url인지 검증한다.
    url_available = input_handler.check_availability()
    if not url_available:
        print("url is not available")
        return False
    audio_file = input_handler.audio_stream()

    # 다운로드한 mp3를 transcriber 모델(whisper)을 사용하여 텍스트파일로 변환한다.
    transcription = transcriber(audio_file)

    # 텍스트 정보를 요약한다.
    summary_result = mapreducer(transcription)

    return summary_result


if __name__ == "__main__":
    import argparse
    from dotenv import load_dotenv
    import os

    load_dotenv()
    api_key = os.environ["OPENAI_API_KEY"]

    parser = argparse.ArgumentParser()
    parser.add_argument("--url")
    args = parser.parse_args()

    input_handler = YoutubeInputHandler()
    transcriber = WhisperAPITranscriber(api_key=api_key)
    mapreducer = LangChainMapReducer(api_key=api_key)

    summary_result = summarize(args.url, input_handler, transcriber, mapreducer)

    print(summary_result)
