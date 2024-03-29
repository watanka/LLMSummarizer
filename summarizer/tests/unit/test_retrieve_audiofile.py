import pytest
import pytube
from io import BytesIO
from summarizer.src.inputhandler import YoutubeInputHandler


def test_retrieve_url_to_stream():
    URL = "https://www.youtube.com/watch?v=QgaTjRH5sqk"

    youtube_parser = pytube.YouTube(URL)

    audio_stream = youtube_parser.streams.filter(only_audio=True).first()

    assert type(audio_stream) is pytube.streams.Stream


def test_pytube_returns_byte() :
    URL = "https://www.youtube.com/watch?v=QgaTjRH5sqk"

    youtube_parser = pytube.YouTube(URL)

    byte_arr = bytearray()
    for byte_obj in pytube.request.stream(youtube_parser.streams.filter(only_audio=True).first().url) :
        byte_arr += byte_obj

    
    assert type(BytesIO(byte_arr).read()) is bytes


def test_input_handler_return_audio_stream():
    URL = "https://www.youtube.com/watch?v=QgaTjRH5sqk"

    input_handler = YoutubeInputHandler()
    input_handler.parse(URL)

    audio_stream = input_handler.audio_stream()

    assert type(audio_stream.read()) is bytes
