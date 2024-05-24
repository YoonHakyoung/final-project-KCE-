from sqlalchemy.orm import Session
from .models import Test, TestData

def create_test(db: Session, test_data: TestData):
    db_test = Test(
        target_url=test_data.target_url,
        test_name=test_data.test_name,
        user_num=test_data.user_num,
        user_plus_num=test_data.user_plus_num,
        interval_time=test_data.interval_time,
        plus_count=test_data.plus_count
    )
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test

def get_tests(db: Session):
    return db.query(Test).all()

def delete_test(db: Session, test_id: int):
    db_test = db.query(Test).filter(Test.test_id == test_id).first()
    if db_test:
        db.delete(db_test)
        db.commit()

def get_test_by_id(db: Session, test_id: int):
    return db.query(Test).filter(Test.test_id == test_id).first()
