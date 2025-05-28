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
                {"role" : "system", "content":"You are a professional email writer. Respond ONLY with the complete email text. Do not add explanations or introductions. Sound like a helpful coworker even tho you are boss. Keep it under 100 words. Speak slovenian dont mention the reciepent name. U are sending as Romeo Bassin"},
                {"role": "user", "content":prompt}
            ]

        )
        return self.response.choices[0].message.content
        