import os
import streamlit as st
import requests

BACKEND_URL = os.getenv("BACKEND_URL")

st.title("Chat CRUD Kezelő")

with st.form("add_chat"):
  email = st.text_input("Email")
  model = st.text_input("Modell (max 30 kar.)", max_chars = 30)
  question = st.text_area("Kérdés")
  answer = st.text_area("Válasz")
  if st.form_submit_button("Mentés"):
    res = requests.post(f"{BACKEND_URL}/chats/", json={
      "email": email, "model": model, "question": question, "answer": answer
    })
    st.success("Chat elmentve!")

if st.button("Frissítés / Listázás"):
  chats = requests.get(f"{BACKEND_URL}/chats/").json()
  for c in chats:
    col1, col2 = st.columns([4, 1])
    col1.write(f"**{c['email']}** ({c['model']}): {c['question']} -> {c['answer']}")
    # if col2.button("Törlés", key = c['id']):
    #   requests.delete(f"{BACKEND_URL}/chats/{c['id']}")
    #   st.rerun()
