import streamlit as st

from pdf_reader import read_pdf
from qa import get_answer


st.title("📄 Intelligent Document Reader")


uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)


if uploaded_file is not None:

    with open("temp.pdf", "wb") as f:

        f.write(uploaded_file.getbuffer())


    text = read_pdf("temp.pdf")


    st.subheader("Extracted Text")

    st.write(text)


    question = st.text_input(
        "Ask a Question"
    )


    if st.button("Get Answer"):

        answer = get_answer(
            question,
            text
        )

        st.subheader("Answer")

        st.success(answer)