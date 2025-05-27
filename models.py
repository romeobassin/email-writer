import datetime

class Email:
    def __init__(self,prompt,response, category, priority):

        self.prompt = prompt
        self.response = response
        self.category = category
        self.priority = priority
        self.timestamp = datetime.datetime.now().isoformat()

    #converts to dict   
    def to_dict(self):
        email_dict = {
            "prompt": self.prompt,
            "response": self.response,
            "metadata":{
                "priority": self.priority,
                "category": self.category,
                "timestamp": self.timestamp
                }
                }
        return email_dict
