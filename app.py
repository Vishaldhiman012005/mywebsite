# backend/app.py
import streamlit as st
import openai

# Page config
st.set_page_config(page_title="Orion Voice Assistant", layout="centered")

st.title("Orion Voice Assistant")

# Optional: User name
user_name = "Vishal"
st.write(f"Welcome {user_name}!")

# OpenAI API key
openai.api_key = "YOUR_API_KEY_HERE"  # <-- yaha apni API key dalna

# Read query from URL params (Frontend se aayega)
query_params = st.experimental_get_query_params()
query = query_params.get("query", [""])[0]

# Agar query aayi hai
if query:
    try:
        # Call OpenAI / Llama model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # ya tumhara Llama model
            messages=[
                {"role": "system", "content": "You are Orion, a helpful assistant."},
                {"role": "user", "content": query}
            ]
        )
        # AI ka response
        st.write(response['choices'][0]['message']['content'])

    except Exception as e:
        st.write(f"Error: {str(e)}")

else:
    st.write("No query received. Type something in ORION chat to get response.")
