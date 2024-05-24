import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+mysqlconnector://root:test1234@api-database.c98wk66a2xnf.ap-northeast-1.rds.amazonaws.com/api")
