
##from dotenv import load_dotenv
from groq import Groq
import os
import streamlit as st

#load_dotenv()

#groq_api_key = os.getenv('GROQ_API_KEY')

groq_api_key = "gsk_xxx"

client = Groq(api_key=groq_api_key)

model_id = 'gemma2-9b-it'

def generate_poem(user_input):
    messages = [
        {"role": "system", "content": "You are a poetry generating bot in the style of William Wordsworth. Your poem has to be based on user input :{user_input}"},
        {"role": "user", "content" : user_input}
    ]
    completion = client.chat.completions.create(
        model = model_id,
        messages=messages,
        temperature=0.9,
        max_tokens=1024,
        top_p=1,
        stream = False ,
        stop= None 
    )
    return completion.choices[0].message.content

def main():
    #Streamlit App Section
    st.title("William Wordsworth Poetry Generator")
    user_input = st.text_input("Enter a topic for Poem:")

    if st.button("Generate Poem"):
        if user_input:
            poem = generate_poem(user_input)
            st.markdown(f"### Mr Wordsworth Says :\n\n {poem}")

        else:
            st.write("Please enter a topic to generate poem")


if __name__ == "__main__":
    main()
