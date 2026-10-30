import os

import streamlit as st

from rag_utility import process_document_to_chroma_db, answer_question


# Set the working directory
working_dir = os.path.dirname(os.path.abspath(__file__))


st.title("🦙 Openai/gpt-oss-20b - Document RAG")


# File uploader widget
uploaded_file = st.file_uploader(
    "Upload a PDF file",
    type=["pdf"]
)


if uploaded_file is not None:

    # Define save path
    save_path = os.path.join(working_dir, uploaded_file.name)

    # Save the uploaded file
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Process the document
    process_document_to_chroma_db(save_path)

    st.success("Document Processed Successfully")


# Text widget to get user input
user_question = st.text_area(
    "Ask your question about the document"
)


if st.button("Answer"):

    if not user_question.strip():
        st.warning("Please enter a question.")

    else:
        answer = answer_question(user_question)

        st.markdown("### Openai/gpt-oss-20b Response")
        st.markdown(answer)
