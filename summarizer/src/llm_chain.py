import os
from langchain.schema import Document
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain.chains import MapReduceDocumentsChain, ReduceDocumentsChain, StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv('OPENAI_API_KEY', 'dummy') # api 실행시에 직접 인풋값으로 넣을 것이므로 dummy값으로 넣어줌


# Define prompt
map_template = """The following is a set of documents
{docs}
Based on this list of docs, please identify the main themes 
Helpful Answer:"""
map_prompt = PromptTemplate.from_template(map_template)

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k", openai_api_key=api_key)

map_chain = LLMChain(llm=llm, prompt=map_prompt)


# Reduce
reduce_template = """The following is set of summaries:
{docs}
Take these and distill it into a final, consolidated summary of the main themes. 
Helpful Answer:"""
reduce_prompt = PromptTemplate.from_template(reduce_template)

# Run chain
reduce_chain = LLMChain(llm=llm, prompt=reduce_prompt)

combine_documents_chain = StuffDocumentsChain(
    llm_chain=reduce_chain, document_variable_name='docs'
)

reduce_documents_chain = ReduceDocumentsChain(
    combine_documents_chain = combine_documents_chain,
    collapse_documents_chain = combine_documents_chain,
    token_max = 4000
)

MapReduceChain = MapReduceDocumentsChain(
    llm_chain = map_chain,

    reduce_documents_chain = reduce_documents_chain,

    document_variable_name = 'docs',

    return_intermediate_steps = False
)

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size = 1000, chunk_overlap = 50
)


if __name__ == '__main__' :
    docs_str = '''
    내가 희가(戲家)의 소설 수십 종을 얻어 읽어보니, 《삼국지연의(三國誌演義)》와 《수당지전(隋唐志傳)》을 제외하고, 그 밖에 《양한지(兩漢志)》는 앞뒤가 맞지 않고, 《제위지(齊魏志)》는 옹졸하며, 《잔당오대지연의(殘唐五代志演義)》는 추솔(粗率)하고, 《송태조용호풍운회(宋太祖龍虎風雲會)》는 소략하며, 《수호전(水滸傳)》은 간사한 속임수에 기교를 부렸다. 이것들은 모두가 독자를 교훈하기에 충분하지 못한 것들인데 한 사람의 솜씨에서 저술이 되었으니 나관중(羅貫中)의 자손이 3대를 벙어리로 살아간 것이 당연한 일이다.

    《서유기(西遊記)》라는 책이 있는데, 종번(宗藩)에서 나왔다고 하는 것으로 이는 곧 현장(玄奘)의 취경기(取經記)를 가지고 그것을 부연한 것이다.

    여기에 대한 사실은 《석보(釋譜)》와 《신승전(神僧傳)》에 대강 나타나 있으되 반신 반의(半信半疑)의 사이에 속한다. 지금 보건대 그 책은 독특하게 불가(佛家)의 수련(修煉)하는 의미를 가설(假說)하였다. 후왕(猴王)의 좌선(坐禪)은 곧 몸을 단련하는 것이며, 노조궁(老祖宮)에서 단(丹)을 훔친 것은 곧 서주(黍珠)를 삼킨 것이며, 대요천궁(大鬧天宮)은 곧 연념(煉念)이며, 법사(法師)를 모시고 서역(西域)에 가는 것은 곧 하거(河車)를 운반(運搬)하는 것이며, 화염산 홍해(火炎山紅孩)는 곧 화후(火候)이며, 흑수(黑水)가 천하(天河)에 통한다는 것은 곧 퇴부후(退符候)이며, 서쪽에서 동쪽으로 돌아왔다는 것은 곧 서호(西虎)가 동룡(東龍)과 교제하는 것이며, 하루에 서천(西天) 10만 리를 돌아온다는 것은 곧 온 하늘의 빽빽한 별을 일시에 셈한다는 것이다. 이는 비록 지리하고 막연하며 그 말들이 올바른 말이 아니지만 종종 다 단결(丹訣)을 가탁하여 이야기하였으므로 진정 내버릴 수는 없다. 나는 특별히 이 책을 간직하고서 진체(眞諦)를 수련하는 여가에 피곤하면 이것으로써 수마(睡魔)를 몰아낼 생각이다.
    '''

    docs = Document(page_content=docs_str)
    split_docs = text_splitter.split_documents([docs])
    MapReduceChain.invoke({'input_documents' : split_docs})