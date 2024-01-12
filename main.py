from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from starlette import status
import uvicorn

from summarizer.src.summary import summarize
from summarizer.src.inputhandler import YoutubeInputHandler
from summarizer.src.transcriber import WhisperAPITranscriber
from summarizer.src.mapreducer import LangChainMapReducer
from summarizer.src.schema import SummaryRequest


app = FastAPI()
app.mount('/assets', StaticFiles(directory='frontend/dist/assets') )


origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return FileResponse("frontend/dist/index.html")

@app.post("/summary", status_code=status.HTTP_200_OK)
def request_summary(summary_request: SummaryRequest):

    input_handler = YoutubeInputHandler()
    transcriber = WhisperAPITranscriber(api_key=summary_request.api_key)
    mapreducer = LangChainMapReducer(api_key=summary_request.api_key)

    try:
        summary_result = summarize(
            summary_request.url,
            summary_request.api_key,
            input_handler,
            transcriber,
            mapreducer,
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"summary process went wrong. need to specify more. error message is \n{e}",
        )

    if not summary_request:
        raise HTTPException(status_code=400, detail="OpenAI API Key invalid.")

    return summary_result


if __name__ == "__main__":
    uvicorn.run(app)
