# backend/app.py
import streamlit as st
import speech_recognition as sr
import openai

st.title("Orion Voice Assistant")

# Optional: User name
user_name = "Vishal"
st.write(f"Welcome {user_name}!")

# OpenAI / Groq API key
openai.api_key = "YOUR_API_KEY_HERE"

# Function to call AI model
def call_groq_model(query):
    response = openai.ChatCompletion.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are Orion, a helpful assistant."},
            {"role": "user", "content": query}
        ]
    )
    return response['choices'][0]['message']['content']

# Voice input button
if st.button("🎤 Speak Now"):
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.info("Listening...")
            audio = r.listen(source)
            query = r.recognize_google(audio)
            st.success(f"You said: {query}")
            response = call_groq_model(query)
            st.write(response)
    except Exception as e:
        st.error("Sorry, could not understand audio")
