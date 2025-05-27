import gpt_client as GPT
import email_manager as em
import models

API = "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"

gpt_client = GPT.GPTClient(API)

manager = em.EmailManager()

prompt = input("Short prompt:")
priority = input("Choose priority: High/Low")
category = input("Choose Work/Personal")

response = gpt_client.generate_email(prompt)

email = models.Email(prompt, response, category, priority)

manager.add_email(email.to_dict())