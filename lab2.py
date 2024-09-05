import streamlit as st
from openai import OpenAI, OpenAIError

st.title("📄 Document Question Answering")
st.write(
    "Upload a document below and ask a question about it – GPT will answer! "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys)."
)

openai_api_key = st.text_input("OpenAI API Key", type="password")

if openai_api_key:
    try:
        client = OpenAI(api_key=openai_api_key)
        client.models.retrieve(model="gpt-4o-mini")  # This checks if the API key is correct
        st.success("API key is valid!")

        uploaded_file = st.file_uploader("Upload a document (.txt or .md)", type=("txt", "md"))
        question = st.text_area(
            "Now ask a question about the document!",
            placeholder="Can you give me a short summary?",
            disabled=not uploaded_file,
        )

        if uploaded_file and question:
            document = uploaded_file.read().decode()
            messages = [
                {"role": "user", "content": f"Here's a document: {document} \n\n---\n\n {question}"},
            ]

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                stream=True,
            )

            st.write_stream(response)

    except OpenAIError as e:
        st.error(f"Failed to validate API key: {str(e)}")
else:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")