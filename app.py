# backend/app.py
import streamlit as st
import requests
import json

# Page config
st.set_page_config(page_title="Orion Voice Assistant", layout="centered")
st.title("Orion Voice Assistant")

user_name = "Vishal"
st.write(f"Welcome {user_name}!")

# Read query from URL params
query_params = st.experimental_get_query_params()
query_text = query_params.get("query", [""])[0]

# Agar query aayi hai
if query_text:
    try:
        grok_api_url = "https://api.x.ai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {st.secrets['GROK_API_KEY']}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "grok-3-mini",   # ya tumhara selected Grok model
            "messages": [
                {"role": "system", "content": "You are Orion, a helpful assistant."},
                {"role": "user", "content": query_text}
            ]
        }

        response = requests.post(grok_api_url, headers=headers, json=payload)
        data = response.json()

        # AI ka response dikhana
        ai_answer = data["choices"][0]["message"]["content"]
        st.write(ai_answer)

    except Exception as e:
        st.write(f"Error: {str(e)}")
else:
    st.write("No query received. Type something in ORION chat to get response.")
