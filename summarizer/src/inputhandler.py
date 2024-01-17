import pytube
from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from io import BytesIO

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
        byte_arr = bytearray()
        for byte_obj in pytube.request.stream(self.parse_obj.streams.filter(only_audio=True).first().url) :
            byte_arr += byte_obj

        return BytesIO(byte_arr)