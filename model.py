from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Text

class UserInputType(Enum) :
    YOUTUBE_URL = 'youtube_url'



class UserRequest(Base) :
    __tablename__ = 'user_request'

    id = Column(Integer, primary_key = True)
    input_type = Column(Enum, nullable = False)
    content = Column(Text, nullable = False)