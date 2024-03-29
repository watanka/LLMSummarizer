from summarizer.src.mapreducer import LangChainMapReducer
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ["OPENAI_API_KEY"]

TEST_TRANSCRIPTION = """
조선조 세종 때에 한 재상이 있었으니, 성은 홍씨요 이름은 아무였다. 대대 명문거족의 후예로서 어린 나이에 급제해 벼슬이 이조판서에까지 이르렀다. 물망이 조야에 으뜸인데다 충효까지 갖추어 그 이름을 온 나라에 떨쳤다. 일찍 두 아들을 두었는데, 하나는 이름이 인형으로서 본처 유씨가 낳은 아들이고, 다른 하나는 이름이 길동으로서 시비 춘섬이 낳은 아들이었다.
그 앞서, 공이 길동을 낳기 전에 한 꿈을 꾸었다. 갑자기 우레와 벽력이 진동하며 청룡이 수염을 거꾸로 하고 공을 향하여 달려들기에, 놀라 깨니 한바탕 꿈이었다. 마음 속으로 크게 기뻐하여 생각하기를, '내 이제 용꿈을 꾸었으니 반드시 귀한 자식을 낳으리라.' 하고, 즉시 내당으로 들어가니, 부인 유씨가 일어나 맞이하였다. 공은 기꺼이 그 고운 손을 잡고 바로 관계하고자 하였으나, 부인은 정색을 하고 말했다.
"상공께서는 위신을 돌아보지도 않은 채 어리고 경박한 사람의 비루한 행위를 하고자 하시니, 첩은 따르지 않겠습니다."
하며 말을 마치고는 손을 떨치고 나가 버렸다. 공은 몹시 무안하여 화를 참지 못하고 외당으로 나와 부인의 지혜롭지 못함을 한탄하였다.
그때 마침 시비 춘섬이 차를 올리기에, 그 고요한 분위기를 틈타 춘섬을 이끌고 곁방에 들어가 바로 관계하였다. 그 무렵 춘섬의 나이는 열여덟이었는데, 한번 몸을 허락한 후에는 문밖에 나가지 아니하고 타인과 접촉할 마음도 먹지 않기에, 공이 기특하게 여겨 애첩으로 삼았다.
과연 그 달부터 태기가 있더니 10달만에 일개 옥동자를 낳았는데, 생김새가 비범하여 실로 영웅호걸의 기상이었다. 공은 한편으로 기뻐하면서도 부인의 몸에서 태어나지 못한 것을 안타깝게 여겼다.
길동이 점점 자라 8살이 되자, 총명하기가 보통이 넘어 하나를 들으면 백 가지를 알 정도였다. 그래서 공은 더욱 귀여워하면서도 출생이 천해, 길동이 늘 아버지니 형이니 하고 부르면, 즉시 꾸짖어 그렇게 부르지 못하게 하였다. 길동이 10살이 넘도록 감히 부형을 부르지 못하고, 종들로부터 천대받는 것을 뼈에 사무치게 한탄하면서 마음 둘 바를 몰랐다.
"대장부가 세상에 나서 공맹을 본받지 못할 바에야, 차라리 병법이라도 익혀 대장인을 허리춤에 비스듬히 차고 동정서벌하여 나라에 큰 공을 세우고 이름을 만대에 빛내는 것이 장부의 통쾌한 일이 아니겠는가. 나는 어찌하여 일신이 적막하고, 부형이 있는데도 아버지를 아버지라 부르지 못하고 형을 형이라 부르지 못하니 심장이 터질지라, 이 어찌 통탄할 일이 아니겠는가!"
하고, 말을 마치며 뜰에 내려와 검술을 익히고 있었다.
그때 마침 공이 또한 달빛을 구경하다가, 길동이 서성거리는 것을 보고 즉시 불러 물었다.
"너는 무슨 흥이 있어서 밤이 깊도록 잠을 자지 않느냐?"
길동은 공경하는 자세로 대답했다.
"소인은 마침 달빛을 즐기는 중입니다. 그런데, 만물이 생겨날 때부터 오직 사람이 귀한 존재인 줄 아옵니다만, 소인에게는 귀함이 없사오니, 어찌 사람이라 하겠습니까?"
공은 그 말의 뜻을 짐작은 했지만, 일부러 책망하는 체하며,
"네 무슨 말이냐?" 했다. 길동이 절하고 말씀드리기를,
"소인이 평생 설워하는 바는, 소인이 대감 정기를 받아 당당한 남자로 태어났고, 낳아 길러 주신 부모님의 은혜를 입었음에도 불구하고, 아버지를 아버지라 못 하옵고, 형을 형이라 못 하오니, 어찌 사람이라 하겠습니까?"
하고, 눈물을 흘리며 적삼을 적셨다. 공이 듣고 나자 비록 불쌍하다는 생각은 들었으나, 그 마음을 위로하면 마음이 방자해질까 염려되어, 크게 꾸짖어 말했다.
"재상 집안에 천한 종의 몸에서 태어난 자식이 너뿐이 아닌데, 네가 어찌 이다지 방자하냐? 앞으로 다시 이런 말을 하면 내 눈앞에 서지도 못하게 하겠다."
이렇게 꾸짖으니 길동은 감히 한 마디도 더 하지 못하고, 다만 당에 엎드려 눈물을 흘릴 뿐이었다. 공이 물러가라 하자, 그제서야 길동은 침소로 돌아와 슬퍼해 마지않았다. 길동이 본래 재주가 뒤어나고 도량이 활달한지라 마음을 가라앉히지 못해 밤이면 잠을 이루지 못하곤 했다. d
"""


def test_mapreduce():
    MapReducer = LangChainMapReducer(api_key=api_key)
    summary_result = MapReducer(TEST_TRANSCRIPTION)

    assert type(summary_result) is str
    assert len(summary_result) < len(TEST_TRANSCRIPTION)  # 요약 결과를 테스트하는 더 나은 방법이 있을까?
