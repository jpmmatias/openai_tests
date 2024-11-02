import streamlit as st
import main as lch
import textwrap

st.title("Rewrite your text!")
st.write("Rewrite your text in different style")
open_ai_key = st.text_input(
            label="Enter your open AI key:",  key="open_ai_key"
)
text = st.text_area("Write your text", key="text")

dialect = st.selectbox('Which dialect?',  ("British English", "American English", "Canadian English", "Australian English", "New Zealand English", "Caribbean English", "Indian English", "South African English", "Irish English")) 
tone = st.selectbox('Which tone?',  ("Neutral", "Happy", "Sad", "Angry", "Excited", "Formal", "Casual", "Professional", "Sarcastic", "Humorous", "Empathetic", "Optimistic", "Pessimistic")
) 

if st.button("Submit", type="primary") and  text and dialect and tone and open_ai_key:
    response = lch.rewrite_text(tone=tone, dialect=dialect,openai_api_key=open_ai_key, text=text)
    st.subheader("Rewrited text:")
    st.text(textwrap.fill(response["rewrited_text"], width=85))
else:
    st.text("Write all the inputs")
