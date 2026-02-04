import os
from sqlalchemy import create_engine, Column, Text, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://askaiwithpy_user:CODXzCzlZSDmjVdGBQQo4qhaAgqQRaVj@dpg-d6060gkoud1c73932ke0-a/askaiwithpy")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()

class Chat(Base):
  __tablename__ = "chats"
  id = Column(Integer, primary_key = True, index = True)
  email = Column(Text)
  model = Column(String(30))
  question = Column(Text)
  answer = Column(Text)

Base.metadata.create_all(bind = engine)
