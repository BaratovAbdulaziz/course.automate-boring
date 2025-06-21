import re
from datetime import datetime

# Check if value is an integer

def num(value):
    if isinstance(value, int):
        print("True")
    else:
        print("False")

# Check if value is a float

def Float_num(value):
    if isinstance(value, float):
        print("True")
    else:
        print("False")

# Check if value is a string

def String(value):
    if isinstance(value, str):
        print("True")
    else:
        print("False")

# Check if value is a boolean
def Boolean(value):
    if isinstance(value, bool):
        print(True)
    else:
        print(False)

# Extract phone numbers matching pattern like +123-456-7890

def phone_number(text):
    template = re.compile(r"\+\d+[-]?\d+[-]?\d+[-]?\d+[-]?\d+")
    result = template.findall(text)
    print(", ".join(result) if result else "No phone number found")

# Extract emails from text

def Email(text):
    email_template = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    email_result = email_template.findall(text)
    print(", ".join(email_result) if email_result else "No email found")

# Extract IP addresses from text

def ip_address(text):
    ip_template = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    ip_address_result = ip_template.findall(text)
    print(", ".join(ip_address_result) if ip_address_result else "No IP address found")

# Extract dates from text in formats dd.mm.yy, dd-mm-yy, dd/mm/yy etc.

def any_date(text):
    date_template = re.compile(r"\b(\d{1,2})[./-](\d{1,2})[./-](\d{2}|\d{4})\b")
    date_result = date_template.findall(text)
    date_strings = [f"{d[0]}.{d[1]}.{d[2]}" for d in date_result]
    print(", ".join(date_strings) if date_strings else "No dates found")

# Birthday checker: compares input date to current date

def Birthday(B_day, B_month, B_year):
    current_date = datetime.now()
    if current_date.day == B_day and current_date.month == B_month and current_date.year == B_year:
        print("are you serious?")
    else:
        B_full_date = f"{B_day}.{B_month}.{B_year}"
        any_date(B_full_date)