

import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

st.title("Research Tool")

prompt = st.text_area("Enter your prompt")

if st.button("Generate"):
    if not prompt.strip():
        st.warning("Enter a prompt first.")
    else:
        with st.spinner("Thinking..."):
            model = ChatGoogleGenerativeAI(
                model="gemini-3.8-flash",
                google_api_key=os.getenv("GOOGLE_API_KEY"),
                max_retries=0,
                max_output_tokens=100,
            )
            response = model.invoke(prompt)
            content = response.content
            
            if isinstance(content, list):
                content = "".join(
                    block.get("text", "")
                    for block in content
                    if isinstance(block, dict) and block.get("type") == "text"
                )

            st.write(content)
