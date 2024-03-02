import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(os.environ.get("DB_URL", "sqlite:///./sqlite.db"))

Base = declarative_base()
