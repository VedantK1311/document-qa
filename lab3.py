import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = 'your-api-key-here'

def get_response(message):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ]
    )
    return response.choices[0].message['content']

# Streamlit application layout
st.title('GPT-based Chatbot')
user_input = st.text_input("Talk to the chatbot:")

if user_input:
    chat_response = get_response(user_input)
    st.text_area("Response", value=chat_response, height=200, disabled=True)
