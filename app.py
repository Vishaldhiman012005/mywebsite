# backend/app.py
import streamlit as st
import requests

# Page config
st.set_page_config(page_title="Orion Voice Assistant", layout="centered")

st.title("Orion Voice Assistant")

# Optional: User name
user_name = "Vishal"
st.write(f"Welcome {user_name}!")

# Grok AI API key
GROK_API_KEY = "YOUR_GROK_API_KEY_HERE"  # <-- yaha apni Grok key dalna

# Read query from URL params (Frontend se aayega)
query_params = st.experimental_get_query_params()
query = query_params.get("query", [""])[0]

if query:
    try:
        # Call Grok AI HTTP API
        url = "https://api.grok.com/v1/chat/completions"  # Example endpoint, actual Grok API URL confirm karo
        headers = {
            "Authorization": f"Bearer {GROK_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama-3.1-8b-instant",  # tumhara model
            "messages": [
                {"role": "system", "content": "You are Orion, a helpful assistant."},
                {"role": "user", "content": query}
            ]
        }
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()

        # Response extract karna (Grok ke format me)
        ai_response = data['choices'][0]['message']['content']
        st.write(ai_response)

    except Exception as e:
        st.write(f"Error: {str(e)}")

else:
    st.write("No query received. Type something in ORION chat to get response.")
