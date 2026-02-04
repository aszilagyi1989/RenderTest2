from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, Chat
from pydantic import BaseModel

app = FastAPI()

class ChatSchema(BaseModel):
  email: str
  model: str
  question: str
  answer: str

def get_db():
  db = SessionLocal()
  try: 
    yield db
  finally: 
    db.close()

@app.post("/chats/")
def create_chat(chat: ChatSchema, db: Session = Depends(get_db)):
  db_chat = Chat(**chat.dict())
  db.add(db_chat)
  db.commit()
  return db_chat

@app.get("/chats/")
def read_chats(db: Session = Depends(get_db)):
  return db.query(Chat).all()

@app.delete("/chats/{chat_id}")
def delete_chat(chat_id: int, db: Session = Depends(get_db)):
  chat = db.query(Chat).filter(Chat.id == chat_id).first()
  if not chat: 
    raise HTTPException(status_code = 404)
  db.delete(chat)
  db.commit()
  return {"status": "deleted"}
