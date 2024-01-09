import pytest
from pytube import YouTube, exceptions

def test_url_is_valid() :
    VALID_URL = 'https://www.youtube.com/watch?v=QgaTjRH5sqk'
    
    youtube_parser = YouTube(VALID_URL)
    try : 
        youtube_parser.check_availability()
    except exceptions.VideoUnavailable :
        pytest.fail('VALID_URL not read. something went wrong.')
    

def test_url_is_invalid() :
    INVALID_URL = 'https://www.youtube.com/watch?v=FAKEYOUTUBELINK'
    youtube_parser = YouTube(INVALID_URL)

    with pytest.raises(exceptions.VideoUnavailable) :
        youtube_parser.check_availability()
        