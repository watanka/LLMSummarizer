

from summarizer.src.llm_chain import MapReduceChain

import abc

import os
from dotenv import load_dotenv

load_dotenv()


class AbstractMapReducer(abc.ABC):
    @abc.abstractmethod
    def __call__(self, transcription):
        raise NotImplementedError


class FakeMapReducer(AbstractMapReducer):
    def __init__(self, llm_chain={"docs": "FAKE SUMMARY"}):
        self.llm_chain = llm_chain

    def __call__(self, transcription: str):
        return self.llm["docs"] + "\n\n" + transcription


class LangChainMapReducer(AbstractMapReducer):
    def __init__(self, api_key = None, llm_chain=MapReduceChain):
        self.llm_chain = llm_chain
        if api_key :
            self.llm_chain.middle[0].openai_api_key = api_key

    def __call__(self, transcription):

        return self.llm_chain.stream({"docs": transcription})
