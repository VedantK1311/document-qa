import streamlit as st
from openai import OpenAI, OpenAIError

# Setup the title and instructions for the app
st.title("📄 Document Question Answering")
st.write(
    "Upload a document below and ask a question about it – GPT will answer! "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys)."
)

# Text input for API key with password hiding
openai_api_key = st.text_input("OpenAI API Key", type="password")

if openai_api_key:
    try:
        # Create an OpenAI client using the provided API key
        client = OpenAI(api_key=openai_api_key)
        
        # Check if the API key is valid by retrieving model details
        client.models.retrieve(model="gpt-4o-mini")
        st.success("API key is valid!")

        # File uploader allows user to upload a text or markdown file
        uploaded_file = st.file_uploader("Upload a document (.txt or .md)", type=("txt", "md"))
        
        # Text area for user to ask a question about the document
        question = st.text_area(
            "Now ask a question about the document!",
            placeholder="Can you give me a short summary?",
            disabled=not uploaded_file,
        )

        # Check if a file has been uploaded and a question asked
        if uploaded_file and question:
            document = uploaded_file.read().decode()
            messages = [
                {"role": "user", "content": f"Here's a document: {document} \n\n---\n\n {question}"},
            ]

            # Generate an answer using the OpenAI API with the gpt-4o-mini model
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                stream=True,
            )

            # Stream the response to the app
            st.write_stream(response)

    except OpenAIError as e:
        # Display error if API key validation fails
        st.error(f"Failed to validate API key: {str(e)}")
else:
    # Inform user to provide an API key to continue
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
