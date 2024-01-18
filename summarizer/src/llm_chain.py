from langchain.schema import Document
from langchain_openai.llms import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import openai

llm = OpenAI(temperature=0, openai_api_key='dummy')

prompt = PromptTemplate.from_template(
    """The following is a video transcription. You are an expert in summarization. Provide the summary in bullet points so that the customer can understand the context without watching the video. The summarization should be in korean.
    {docs}
    """
)

output_parser = StrOutputParser()

llm_chain = prompt | llm | output_parser
