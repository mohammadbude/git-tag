import re

def extract_emails(text):
    pattern = r"[a-zA-Z0-9]\.+[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]"
    result = re.match(pattern,text)
    if result:
        print('Valid mail')
    else:
        print("invlaid")


text = input()
extract_emails(text)
