import pytube
from summary.inputhandler import YoutubeInputHandler

def test_retrieve_url_to_stream() :
    URL = 'https://www.youtube.com/watch?v=QgaTjRH5sqk'

    youtube_parser = pytube.YouTube(URL)

    video_stream = youtube_parser.streams.filter(only_audio = True).first()

    assert type(video_stream) is pytube.streams.Stream



