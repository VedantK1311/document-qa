import streamlit as st
from openai import OpenAI, OpenAIError

def run_lab1():
    # Show title and description.
    st.title("📄 Vedant's Question Answering Chatbot")
    st.write(
        "Upload a document below and ask a question about it – GPT will answer! "
        "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys)."
    )

    # Ask user for their OpenAI API key via st.text_input.
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.", icon="🗝️")
    else:
        client = OpenAI(api_key=openai_api_key)
        try:
            # Validate the key by attempting to retrieve a specific model's details.
            client.models.retrieve(model="text-davinci-002")  # Using a lightweight call for validation
            st.success("API key is valid!", icon="✅")
        except OpenAIError as e:
            st.error(f"Invalid API key! Error: {e}", icon="❌")
        else:
            uploaded_file = st.file_uploader("Upload a document (.txt or .md)", type=("txt", "md"))
            question = st.text_area(
                "Now ask a question about the document!",
                placeholder="Can you give me a short summary?",
                disabled=not uploaded_file,
            )

            if uploaded_file and question:
                document = uploaded_file.read().decode()
                messages = [
                    {"role": "user", "content": f"Here's a document: {document}\n\n---\n\n{question}"},
                ]

                try:
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=messages,
                        stream=True,
                    )

                    # Assuming 'response' is an iterable stream of messages
                    for message in response:
                        st.write(message.get('content', 'No response content.'))

                except OpenAIError as e:
                    st.error(f"Failed to generate response: {e}")
