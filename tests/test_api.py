from fastapi.testclient import TestClient
from dotenv import load_dotenv
import os

from app import app
load_dotenv()
test_api_key = os.environ['OPENAI_API_KEY']

client = TestClient(app)


def test_happy_response() :
    TEST_URL = 'https://www.youtube.com/watch?v=QgaTjRH5sqk'

    response = client.post('/summary/', json = {'url' : TEST_URL,
                                                'api_key' : test_api_key
                                            })
    assert response.status_code == 200
    

def test_invalid_url() : 
    INVALID_URL = 'https://www.youtube.com/watch?v=fake'

    response = client.post('/summary/', json = {'url' : INVALID_URL,
                                                'api_key' : test_api_key
                                            })
    assert response.status_code == 400

def test_invalid_api_key() :
    TEST_URL = 'https://www.youtube.com/watch?v=QgaTjRH5sqk'
    invalid_api_key='fake_apikey'

    response = client.post('/summary/', json = {'url' : TEST_URL,
                                                'api_key' : invalid_api_key
                                            })
    assert response.status_code == 400


