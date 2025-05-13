#importing required libraries and modules
import re,os,sys

# manual installation of pyperclip
#optional if not installed already
#os.system("sudo apt install python3-pyperclip")
import pyperclip

#finding contact numbers

scanning_data = pyperclip.paste()
number_templates = re.compile(r"\+?(\d{3})[\s-]?(\d{2,3})[\s-]?(\d{3,4})[\s-]?(\d{2,3})[\s-]?(\d{2,3})")
number_result = number_templates.findall(f"{scanning_data}") #we use findall() to find all required matches
if number_result:
    print(f"\n these phone numbers were found")
    for number in number_result:
        print(" " "-".join(number))
else:
    print("no numbers found")
# finding email addresses
email_template = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
email_result = email_template.findall(f"{scanning_data}")
#printing found email_data
if email_result:
    print(f"emails found:\n")
    for email in email_result:
        print(" ".join(email))
else:
    print("No emails found")