import re

filepath = r'c:\3ph_Digi_starter\3ph_digi_starter.c'
with open(filepath, 'rb') as f:
    text = f.read().decode('utf-8', errors='ignore')

# Fix main block
# Find: handle_menu(); \s+ lcd_cmd(LCD_CLEAR); \s+ enable_interrupts(int_AD);
pattern = r'(handle_menu\(\);\s*)lcd_cmd\(LCD_CLEAR\);\s*(enable_interrupts\(int_AD\);)'
text = re.sub(pattern, r'\1\2', text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Replacement logic complete.")
