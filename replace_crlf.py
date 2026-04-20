filepath = r'c:\3ph_Digi_starter\3ph_digi_starter.c'
with open(filepath, 'rb') as f:
    text = f.read()

# Fix the newline issue if it exists
text = text.replace(b'\r\r\n', b'\r\n')

with open(filepath, 'wb') as f:
    f.write(text)

