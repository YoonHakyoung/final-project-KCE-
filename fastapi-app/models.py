from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from .database import Base

class TestData(BaseModel):
    target_url: str
    test_name: str
    user_num: int
    user_plus_num: int
    interval_time: int
    plus_count: int

class Test(Base):
    __tablename__ = "test"

    test_id = Column(Integer, primary_key=True, index=True)
    target_url = Column(String, index=True)
    test_name = Column(String, index=True)
    user_num = Column(Integer)
    user_plus_num = Column(Integer)
    interval_time = Column(Integer)
    plus_count = Column(Integer)
