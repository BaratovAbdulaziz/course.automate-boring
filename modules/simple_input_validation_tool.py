import re
from datetime import datetime

# Check if value is an integer

def num(value):
    if type(value) == int:
        print("True")
    else:
        print("False")

# Check if value is a float

def Float_num(value):
    if type(value)== float:
        print("True")
    else:
        print("False")

# Check if value is a string

def String(value):
    if type(value) == str:
        print("True")
    else:
        print("False")

# Check if value is a boolean
def Boolean(value):
    if isinstance(value, bool):
        print(True)
    else:
        print(False)

# is there phone numbers matching pattern like +123-456-7890

def phone_number(text):
    template = re.compile(r"\+\d+[-]?\d+[-]?\d+[-]?\d+[-]?\d+")
    result = template.findall(text)
    if result:
        print(True)
    else:
        print(False)

# Is there amy emails in the  text

def Email(text):
    email_template = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    email_result = email_template.findall(text)
    if email_result:
        print(True)
    else:
        print(False)

# Is there  IP addresses in the text

def ip_address(text):
    ip_template = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    ip_address_result = ip_template.findall(text)
    if ip_address_result:
        print(True)
    else:
        print(False)
# weather there are true dates in the  text in formats dd.mm.yy, dd-mm-yy, dd/mm/yy etc.

def any_date(text):
    date_template = re.compile(r"\b(\d{1,2})[./-](\d{1,2})[./-](\d{2}|\d{4})\b")
    date_result = date_template.search(text)
    if date_result:
        print(True)
    else:
        print(False)