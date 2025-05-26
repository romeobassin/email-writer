import json
import os

class EmailManager:
    def __init__(self, file_path = "emails.json"):
        
        self.file_path = file_path
        self.emails = []
        self.emailsLATER = [{
            "prompt": "actual prompt inputs",
            "gen_msg": "gpt responses",
            "metadata": {
                "priority": "normal/high/low",
                "category": "work/personal",
                "timestamp": "auto-generated"
            }
            }]
        
        if os.path.exists(self.file_path):
                
            try:
                with open("emails.json", "r") as f:
                    self.emails = json.load(f)
                    
            except Exception as e:
                print("the .JSON file doesnt exist yet")
                self.emails = []
        else:
            print("No existing email file found")
            self.emails = []
    
    def save_emails(self):
        try:
            with open(self.file_path,"w") as f:
                json.dump(self.emails,f,indent=2)
        except Exception as e:
            print("Error saving mails:",e)
        
    def add_email(self,email_obj):
        if email_obj in self.emails:
            print("That mail already exists.")
            return False
        else:
            self.emails.append(email_obj)
            self.save_emails()
            print("Email saved succesfully")
            return True
    def list_emails(self,filter_func=None):
        for email in self.emails:
            if filter_func is None or filter_func(email):
                yield email

    

        
    
    

