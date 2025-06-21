#importing required modules
import re,time,os
from datetime import datetime
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

##################################################
################||||| MENU ||||###################
##################################################
def Menu():
    while True:
    #content importing
    
        text = str(input(f"enter the content \n :"))
    
    #Timeout
        time.sleep(1)
        os.system("clear")
        print("processing...")
        time.sleep(1)
        print("content imported successfully!!!")
        time.sleep(1)
        os.system("clear")
        time.sleep(1)
        print('''
1. find phone numbers
2. find emails
3. find IP addresses
4. extract dates
"E" Exit''')
        answer = input("(1/2/3/4):")
        if answer == "1":
            phone_number(text)
            break
        elif answer == "2":
            Email(text)
            break

        elif answer == "3":
            ip_address(text)
            break

        elif answer == "4":
            any_date(text)
            break

        elif answer.lower() == "e":
            break

        else:
            print("Error 404")
Menu()