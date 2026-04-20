filepath = r'c:\3ph_Digi_starter\3ph_digi_starter.c'
with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'void main()' in line:
        for j in range(i, i+150):
            if 'handle_menu()' in lines[j] or 'prog == 1' in lines[j]:
                print(f"{j}: {lines[j].strip()}")

