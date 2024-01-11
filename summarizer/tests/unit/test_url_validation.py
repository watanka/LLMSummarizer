from pytube import YouTube, exceptions
import pytest

from src.inputhandler import YoutubeInputHandler


def test_url_is_valid():
    VALID_URL = "https://www.youtube.com/watch?v=QgaTjRH5sqk"

    youtube_parser = YouTube(VALID_URL)
    try:
        youtube_parser.check_availability()
    except exceptions.VideoUnavailable:
        pytest.fail("VALID_URL not read. something went wrong.")


def test_url_is_invalid():
    INVALID_URL = "https://www.youtube.com/watch?v=FAKEYOUTUBELINK"
    youtube_parser = YouTube(INVALID_URL)

    with pytest.raises(exceptions.VideoUnavailable):
        youtube_parser.check_availability()


def test_input_handler_handle_valid_url():
    VALID_URL = "https://www.youtube.com/watch?v=QgaTjRH5sqk"

    input_handler = YoutubeInputHandler()
    input_handler.parse(VALID_URL)

    try:
        input_handler.check_availability()
    except exceptions.VideoUnavailable:
        pytest.fail("VALID_URL not read. something went wrong")


def test_input_handler_handle_invvalid_url():
    INVALID_URL = "https://www.youtube.com/watch?v=FAKEYOUTUBELINK"

    input_handler = YoutubeInputHandler()
    input_handler.parse(INVALID_URL)

    assert not input_handler.check_availability()
