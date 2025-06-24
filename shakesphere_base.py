from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')

#print(groq_api_key)
#groq_api_key = "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"


client = Groq(api_key=groq_api_key)

model_id = 'gemma2-9b-it'

user_input = "I walk in Hyde Park thinking of mankind"

messages = [
        {"role": "system", "content": "You are a poetry generating bot in the style of William Wordsworth. Your poem has to be based on user input :{user_input}"},
        {"role": "user", "content" : user_input}
    ]

def generate_poem(user_input):

    completion = client.chat.completions.create(
        model = model_id,
        messages=messages,
        temperature=0.1,
        max_tokens=1024,
        top_p=1,
        stream = False ,
        stop= None 
    )
    return completion.choices[0].message.content


def main():
    poem = generate_poem(user_input)
    
    print ( poem)



if __name__ == "__main__":
    main()