from langchain.schema import Document
from langchain_openai.llms import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import openai

import abc

import os
from dotenv import load_dotenv

load_dotenv()
llm = OpenAI(temperature=0)

prompt = PromptTemplate.from_template('''The following is a video transcription. You are an expert in summarization. Provide the summary in bullet points so that the customer can understand the context without watching the video. The summarization should be in korean.
    {docs}
    ''')

output_parser = StrOutputParser()

llm_chain = prompt | llm | output_parser


class AbstractMapReducer(abc.ABC) :
    @abc.abstractmethod
    def __call__(self, transcription) :
        raise NotImplementedError


class FakeMapReducer(AbstractMapReducer) :
    def __init__(self, llm_chain = {'docs' : 'FAKE SUMMARY'} ) :
        self.llm_chain = llm_chain

    def __call__(self, transcription : str) :
        return self.llm['docs'] +  '\n\n' + transcription



class LangChainMapReducer(AbstractMapReducer) :

    def __init__(self, llm_chain = llm_chain, api_key = None) :
        self.llm_chain = llm_chain
        if api_key :
            self.llm_chain.middle[0].openai_api_key = api_key


    def __call__(self, transcription) :
        
        return self.llm_chain.invoke({'docs' : transcription})
        


