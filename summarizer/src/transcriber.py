from openai import OpenAI
from dotenv import load_dotenv

import abc

load_dotenv()
whisper_model = OpenAI()


class AbstractTransriber(abc.ABC):
    @abc.abstractmethod
    def __call__(self, transcription):
        raise NotImplementedError


class FakeTranscriber(AbstractTransriber):
    def __call__(self, video_path: str) -> str:
        return f"Given {video_path}, BUT THIS IS FAKE TRANSCRIPTION."


class WhisperLocalTranscriber(AbstractTransriber):
    def __init__(self, transcribe_model):
        self.transcribe_model = transcribe_model

    def __call__(self, video_path: str) -> str:
        transcription = self.transcribe_model.transcribe(
            video_path, response_format="text"
        )

        return transcription


class WhisperAPITranscriber(AbstractTransriber):
    def __init__(self, api_key, transcribe_model=whisper_model):
        self.transcribe_model = transcribe_model
        self.transcribe_model.api_key = api_key

    def __call__(self, video_binary: str) -> str:
        transcription = self.transcribe_model.audio.transcriptions.create(
            file=video_binary, model="whisper-1", response_format="text"
        )
        return transcription
