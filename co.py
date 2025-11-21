from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os, time

DB_HOST = os.getenv("DB_HOST", "host.docker.internal")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASSWORD", "cm6361")
DB_NAME = os.getenv("DB_NAME", "soilrecommendation")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

while True:
    try:
        engine = create_engine(DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        print("✅ Connected to MySQL via SQLAlchemy")
        break
    except Exception as e:
        print("⏳ Waiting for MySQL... Retrying", e)
        time.sleep(2)
