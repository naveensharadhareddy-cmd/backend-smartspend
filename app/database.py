import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()  # ← add this

DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

engine = create_engine(DATABASE_URL)
