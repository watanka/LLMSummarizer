

from summary.inputhandler import AbstractInputHandler, YoutubeInputHandler
from summary.transcriber import AbstractTransriber, WhisperAPITranscriber
from summary.mapreducer import AbstractMapReducer, LangChainMapReducer



transcriber = WhisperAPITranscriber()


url = 'https://www.youtube.com/watch?v=QgaTjRH5sqk'
transcribe_model = 'FAKEMODEL'



def transcribe(transcription_path, transcribe_model) :    
    # 다운로드한 값 
    transcription = transcribe_model(transcription_path)
    return transcription


def summarize(url, 
         input_handler : AbstractInputHandler, 
         transcriber : AbstractTransriber,
         mapreducer : AbstractMapReducer
         ) :
    # parser 정의. pytube 사용
    input_handler.parse(url)
    
    # url이 유효한 youtube url인지 검증한다.
    url_available = input_handler.check_availability()
    if not url_available :
        print('url is not available')
        return
    audio_file = input_handler.audio_stream()

    # 다운로드한 mp3를 transcriber 모델(whisper)을 사용하여 텍스트파일로 변환한다.
    transcription = transcriber(audio_file)

    # 텍스트 정보를 요약한다.
    summary_result = mapreducer(transcription)

    return summary_result

if __name__ == '__main__' :
    import argparse

    args = argparse.ArgumentParser()
    args.add_argument('--url')

    whisper_model = OpenAI(api_key = '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')
    input_handler = YoutubeInputHandler()
    transcriber = WhisperAPITranscriber(transcribe_model=whisper_model)
    mapreducer = LangChainMapReducer()

    summary_result = summarize( url,
                                input_handler,
                                transcriber,
                                mapreducer)
    
    print(summary_result)