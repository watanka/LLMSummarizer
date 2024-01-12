import pytube
from openai import OpenAI

from summarizer.src.inputhandler import YoutubeInputHandler
from summarizer.src.transcriber import WhisperAPITranscriber

import os, shutil
import json
from dotenv import load_dotenv

load_dotenv()
whisper_model = OpenAI()
transcriber = WhisperAPITranscriber(whisper_model)


def test_openai_whisper_takes_pytube_stream_as_input():
    URL = "https://www.youtube.com/watch?v=QgaTjRH5sqk"

    TMP_DOWNLOAD_DIR = "./tmp/"
    TMP_FNAME = "test.mp3"

    youtube_parser = pytube.YouTube(URL)

    video_stream = youtube_parser.streams.filter(only_audio=True).first()

    # 다운로드를 위한 폴더 생성
    os.makedirs(TMP_DOWNLOAD_DIR, exist_ok=True)

    video_stream.download(output_path=TMP_DOWNLOAD_DIR, filename=TMP_FNAME)

    # 다운로드한 파일 binary로 읽기
    audio_file = open(os.path.join(TMP_DOWNLOAD_DIR, TMP_FNAME), "rb")

    transcript = whisper_model.audio.transcriptions.create(
        file=audio_file, model="whisper-1", response_format="text"
    )

    assert type(transcript) == str


def test_transcriber_abstract_details():
    URL = "https://www.youtube.com/watch?v=QgaTjRH5sqk"

    input_handler = YoutubeInputHandler()
    input_handler.parse(URL)

    transcriber = WhisperAPITranscriber(api_key=os.environ["OPENAI_API_KEY"])
    transcription = transcriber(input_handler.audio_stream())

    assert type(transcription) is str
