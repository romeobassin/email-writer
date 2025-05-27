import json
import os

class EmailManager:
    def __init__(self, file_path = "emails.json"):
        
        self.file_path = file_path
        self.emails = []
        #checks if file exists
        if os.path.exists(self.file_path):
                
            try:
                with open("emails.json", "r") as f:  #reads whole json file
                    self.emails = json.load(f)
                    
            except Exception as e:   #handles error otherwise creates new json file
                print("the .JSON file doesnt exist yet")
                self.emails = []
        else:
            print("No existing email file found")
            self.emails = []
    
    def save_emails(self):          #writes email dict on json file
        try:
            with open(self.file_path,"w") as f:
                json.dump(self.emails,f,indent=2)
                print("Saving to:", os.path.abspath(self.file_path))
        except Exception as e:
            print("Error saving mails:",e)
        
    def add_email(self,email_obj):   #adds email instance to mail list
        if email_obj in self.emails:
            print("That mail already exists.")
            return False
        else:
            #checks for required keys
            required_keys = ["prompt", "response","metadata"]
            if not all(key in email_obj for key in required_keys):
                print("Invakid email")
                return False
            
            #checks for metadata structure
            metadata = email_obj["metadata"]
            required_meta = ["priority","category", "timestamp"]
            if not isinstance(metadata, dict) or not all(key in metadata for key in required_meta):
                print("Metadata is missing ", type(metadata) )
                return False




            self.emails.append(email_obj)
            print(type(self.emails[0]))
            self.save_emails()
            print("Email saved succesfully")
            return True
        
    def list_emails(self,filter_func=None):
        for email in self.emails:
            if filter_func is None or filter_func(email):
                yield email

    

        
    
    

