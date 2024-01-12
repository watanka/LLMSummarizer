import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ['OPENAI_API_KEY']

st.title("유튜브 요약 서비스:sunglasses:")


def request_summary(url: str, api_key: str):
    response = requests.post(
        f"http://summarizer:8090/summary", json={"url": url, "api_key": api_key}
    )
    return response.json()


def disable():
    st.session_state.disabled = True


if "disabled" not in st.session_state:
    st.session_state.disabled = False

summary_result = ""
with st.form("my-form"):
    url = st.text_input(
        "요약이 필요한 Youtube URL을 입력해주세요.",
        key="url",
        autocomplete="https://www.youtube.com/watch?v=QgaTjRH5sqk",
        disabled=True
    )
    api_key = st.text_input(
        "OpenAI api key를 입력해주세요. [해당 링크](https://platform.openai.com/api-keys)에서 만들 수 있습니다.",
        key="api_key",
        autocomplete=api_key,
        disabled=True
    )

    submitted = st.form_submit_button(
        "요약", on_click=disable, disabled=st.session_state.disabled
    )

    if submitted:
        summary_result = request_summary(url, api_key)
        st.session_state.disabled = False

        st.write(summary_result)
