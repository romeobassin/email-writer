import openai
import os

class GPTClient:
    def __init__(self,api_key):
        os.environ["OPENAI_API_KEY"] = api_key
        self.client = openai.OpenAI()
    
    def generate_email(self,prompt,model='gpt-4o'):
        self.response = self.client.chat.completions.create(
            model=model,
            temperature=0.7,
            messages= [
                {"role" : "system", "content":"You are a friendly boss that appreciates your employees. Very understandable and respectful, feeling like you owe them"},
                {"role": "user", "content":prompt}
            ]

        )
        return self.response.choices[0].message.content
        