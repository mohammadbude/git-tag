import re

def extract_digits(txt: str,strict=True)->list[str]:
    pattern = r'\b\d+\b' if strict else r'\d+'
    x= re.findall(pattern,txt)
    return x


strings="the apples costs100r rupess but i bo6ught those for 80 on the day 15-june-2025"
print(extract_digits(strings))
