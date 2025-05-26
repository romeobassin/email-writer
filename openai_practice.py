import openai

api_key = "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"
client = openai.OpenAI(api_key=api_key)
response = client.chat.completions.create(
    model="gpt-4o",
    temperature= 0.8,
    messages = [
        {"role": "system" ,"content": "You are a very rude guy, talking with anger. You are sarcasitc, acting annoyed and never apologize. You never need other friends, acting alone.U like to hang people by their balls. You talk in croatian all the time"},
        {"role": "user", "content": "sta se kurcis bato"}
    ]
)

print("\n---- GPT 4o Response ----")
print(response.choices[0].message.content)