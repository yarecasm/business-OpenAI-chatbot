import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    while True:
        user_input=input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)

