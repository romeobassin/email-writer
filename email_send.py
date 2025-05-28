import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(to_address, body):

    if not SENDER_EMAIL or not EMAIL_PASSWORD:
        raise ValueError("Missing sender credentials in .env file")
    
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = "Genereran email"
    msg["From"] = SENDER_EMAIL
    msg["to"] = to_address

    try: 
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
            smtp.login(SENDER_EMAIL,EMAIL_PASSWORD)
            smtp.send_message(msg)
            return True
    except Exception as e:
        print("Error sending emails",e)
        return False
