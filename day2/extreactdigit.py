import re

def extract_digits(txt: str)->list[str]:
    pattern = r'\b\d+\b'
    x= re.findall(pattern,txt)
    return x


strings="the apples costs100 rupess but i bought those for 80 on the day 15-june-2025"
print(extract_digits(strings))
