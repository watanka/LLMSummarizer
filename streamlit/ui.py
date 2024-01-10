import streamlit as st
import requests




st.title('유튜브 요약 서비스:sunglasses:')


def request_summary(url : str, api_key : str) :
    response = requests.post(f'http://localhost:8000/summary', json = {'url' : url, 'api_key' : api_key})
    return response.json()


with st.form('my_form') :
    summary_result = ''
    # with input_form :
    url = st.text_input("요약이 필요한 Youtube URL을 입력해주세요.", key = 'url')
    api_key = st.text_input("OpenAI api key를 입력해주세요. [해당 링크](https://platform.openai.com/api-keys)에서 만들 수 있습니다.", key = 'api_key')
    # with submit_button :
    submitted = st.form_submit_button('요약')
    if submitted :
        summary_result = request_summary(url = url, api_key = api_key)
        
        st.write(summary_result)