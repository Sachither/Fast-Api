from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

# while True:
#     try:
#         conn = psycopg2.connect(
#             host="localhost",
#             database="FastApi",
#             user="postgres",
#             password="admin",
#             cursor_factory=RealDictCursor
#         )
#         cur = conn.cursor()
#         print("Database connection successful")
#         break
#     except Exception as e:
#         print("Database connection failed")
#         print(f"Error: {e}")
#         time.sleep(2)