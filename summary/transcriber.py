from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
whisper_model = OpenAI()

class AbstractTransriber :
    pass


class FakeTranscribeModel :
    def __call__(self, video_path : str) -> str :
        return f'Given {video_path}, BUT THIS IS FAKE TRANSCRIPTION.'



class WhisperLocalTranscriber(AbstractTransriber) :

    def __init__(self, transcribe_model) :
        self.transcribe_model = transcribe_model

    def __call__(self, video_path : str) -> str :
        transcription = self.transcribe_model.transcribe(video_path, response_format = 'text')

        return transcription


class WhisperAPITranscriber(AbstractTransriber) :

    def __init__(self, transcribe_model = whisper_model) :
        self.transcribe_model = transcribe_model

    def __call__(self, video_binary : str) -> str :
        transcription = self.transcribe_model.audio.transcriptions.create(
                                                          file = video_binary,
                                                          model = 'whisper-1',
                                                          response_format = 'text'
                                                          )
        return transcription