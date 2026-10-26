
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
st.title("Research Paper Explainer")

template = load_prompt("template.json")

paper_input = st.selectbox("Select Research Paper", [
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis"
])

style_input = st.selectbox("Explanation Style", [
    "Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"
])

length_input = st.selectbox("Explanation Length", [
    "Short", "Medium", "Long"
])

if st.button("Summarize"):
    with st.spinner("Generating..."):
        try:
            prompt = template.format(
                paper_input=paper_input,
                style_input=style_input,
                length_input=length_input
            )

            model = ChatGoogleGenerativeAI(
                model="gemini-3.8-flash",
                google_api_key=os.getenv("GOOGLE_API_KEY"),
                max_retries=0,
                max_output_tokens=300,
            )

            response = model.invoke(prompt)
            content = response.content

            if isinstance(content, list):
                content = "".join(
                    block.get("text", "")
                    for block in content
                    if isinstance(block, dict)
                    and block.get("type") == "text"
                )

            st.subheader(paper_input)
            st.write(content)

        except Exception as e:
            st.error(f"Error: {e}")
