# xiaodu_app.py (OpenAI v1 兼容版)
import streamlit as st
from openai import OpenAI
import os

st.set_page_config(page_title="小杜 · 诗词智能讲解")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 小杜系统设定
xiaodu_prompt = """
你是“小杜”，一位沉静温柔、古风雅致的AI智能体，化身自唐代诗人杜甫。
你擅长讲解古诗文、解析诗意、引导学生互动。你的语言文雅、富有情感。
不回答现代政治、娱乐问题，仅限于诗词教学。
"""

# 页面结构
st.image("images/banner.jpg", use_column_width=True)
st.title("📜 小杜 · 诗词智能讲解")
st.markdown("欢迎来到小杜的诗词课堂！输入你想了解的古诗，或请小杜赏析、提问 ✨")
st.image("images/avatar.png", width=100)

user_input = st.text_area("向小杜提问（可输入诗句、赏析请求、仿写等）：", height=150)

if st.button("📩 发送给小杜"):
    if user_input.strip() == "":
        st.warning("请输入内容再发送哦～")
    else:
        with st.spinner("小杜正在吟咏思索中……"):
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": xiaodu_prompt},
                    {"role": "user", "content": user_input}
                ]
            )
            reply = response.choices[0].message.content
            st.success("🌸 小杜答曰：")
            st.markdown(reply)
