from groq import Groq

client = Groq(
    api_key=("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"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": input("Write your message"),
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)