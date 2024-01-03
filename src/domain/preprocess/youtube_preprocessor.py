from src.domain.preprocess.base_preprocesser import BasePreprocessor
from model import UserRequest

from pytube import YouTube


class YoutubeUrlPreprocessor(BasePreprocessor) :

    def __call__(self, user_request : UserRequest) :
        print('process ')