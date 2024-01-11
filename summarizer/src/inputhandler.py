from pytube import YouTube
from pytube.exceptions import VideoUnavailable

import abc

from uuid import uuid4
import os

tmpdir = "./tmp"
os.makedirs(tmpdir, exist_ok=True)


class AbstractInputHandler(abc.ABC):
    @abc.abstractmethod
    def parse(self, url):
        raise NotImplementedError

    @abc.abstractmethod
    def check_availability(self):
        raise NotImplementedError

    @abc.abstractmethod
    def audio_stream(self):
        raise NotImplementedError


class YoutubeInputHandler(AbstractInputHandler):
    def __init__(self, parser=YouTube):
        self.parser = parser
        self.parse_obj = None

    def parse(self, url):
        self.parse_obj = self.parser(url)

    def check_availability(self):
        try:
            self.parse_obj.check_availability()
            return True

        except VideoUnavailable:
            return False

    def audio_stream(self):
        """
        **download audio file as side effect
        """
        try:
            tmp_fname = str(uuid4())[:8] + ".mp3"
            self.parse_obj.streams.filter(only_audio=True).first().download(
                output_path=tmpdir, filename=tmp_fname
            )

            audio_file = open(os.path.join(tmpdir, tmp_fname), "rb")

            return audio_file

        finally:
            os.remove(os.path.join(tmpdir, tmp_fname))
