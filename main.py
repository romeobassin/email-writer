import gpt_client as GPT
import email_manager as em
from tkinter import ttk, messagebox,scrolledtext
import tkinter as tk
import models
from dotenv import load_dotenv
import os
import email_send as send

load_dotenv()
API = os.getenv("OPENAI_API_KEY")
gpt_client = GPT.GPTClient(API)
manager = em.EmailManager()

response = ""

root = tk.Tk()
root.title("EmailAutomated")
root.geometry("700x600")

root.grid_columnconfigure(0,weight=	1)
root.grid_columnconfigure(1,weight=	1)
root.grid_columnconfigure(2,weight=	1)

frame = tk.Frame(root)
frame_dropdown_1 = tk.Frame(root)
frame_dropdown_2 = tk.Frame(root)

prompt_label = tk.Label(frame, text="Enter prompt..")
prompt_label.grid(row=0,column=1,padx=(0,10))

prompt_entry = tk.Entry(frame,width=(30))
prompt_entry.grid(row=1,column=1,padx=(0,10))

frame.grid(row=0,column=1)
frame_dropdown_1.grid(row=0,column=0,sticky="e")


priority_label = tk.Label(frame,text="Choose priority")
priority_label.grid(row=0,column=2)

dropdown_priority = ttk.Combobox(frame, values=["High","Low"],state=["readonly"])
dropdown_priority.grid(row=1,column=2)


category_label = tk.Label(frame, text="Choose category")
category_label.grid(row=0,column=3,padx=(10,0))


category_dropdown = ttk.Combobox(frame, values=["Work","Personal"],state=["readonly"])
category_dropdown.grid(row=1,column=3,padx=(10,0))


output_text = scrolledtext.ScrolledText(root, height= 15)
output_text.grid(row=1,column=1,pady=(15,15))

reciepent_label = tk.Label(frame,text="Reciepent")
reciepent_label.grid(row=0,column=0,padx=(0,15))

reciepent_entry = tk.Entry(frame)
reciepent_entry.grid(row=1,column=0,padx=(0,15))

def generate_Email():
    prompt = prompt_entry.get()
    priority = dropdown_priority.get()
    category = category_dropdown.get()

    if not prompt:
        messagebox.showwarning("Input Error", "Prompt cannot be empty")
    global response
    response = gpt_client.generate_email(prompt)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END,response)

    email = models.Email(prompt,response,category,priority)
    email_dict = email.to_dict()
    manager.add_email(email_dict)
    

def list_emails():
    output_text.delete("1.0",tk.END)
    for email in manager.list_emails():
        content = f"Prompt: {email["prompt"]}\nResponse: {email["response"]}\nMetadata:{email["metadata"]}\n{'-'*50}\n"
        output_text.insert(tk.END, content)

def send_email_from():
    reciepent = reciepent_entry.get()
    body = output_text.get("1.0",tk.END).strip()

    if not reciepent:
        messagebox.showwarning("Missing info")
        return
    success = send.send_email(reciepent,body)
    if success: 
        messagebox.showinfo("Success, sent succesfully")
    else:
        messagebox.showerror("Failed to send email")


generate_button = tk.Button(frame,text="Generate Email", command=generate_Email)
generate_button.grid(row=1,column=4,padx=(15,0))

view_button = tk.Button(frame,text="View current mails", command=list_emails)
view_button.grid(row=1,column=5,padx=(10,0))



send_button = tk.Button(frame,text="Send Email",command = send_email_from)
send_button.grid(row=1,column=6, padx=(10,0))


root.mainloop()