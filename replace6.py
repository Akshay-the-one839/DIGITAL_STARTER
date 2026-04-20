import re

filepath = r'c:\3ph_Digi_starter\3ph_digi_starter.c'
with open(filepath, 'rb') as f:
    text = f.read().decode('utf-8', errors='ignore')

# Fix spacing
pattern = r'\}\s*else if \(menu_number == (\d+)\)'
repl = r'}\r\n      else if (menu_number == \1)'

text = re.sub(pattern, repl, text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

