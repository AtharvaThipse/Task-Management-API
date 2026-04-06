from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine
import time

DATABASE_URL = "postgresql://postgres:1101@localhost:5433/task1"


for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        print("✅ Connected to DB")
        connection.close()
        break
    except Exception as e:
        print("⏳ Waiting for DB to be ready...")
        time.sleep(2)
else:
    raise Exception("❌ Could not connect to DB")


SessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base = declarative_base()
