filepath = r'c:\3ph_Digi_starter\3ph_digi_starter.c'
with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if 'void handle_menu()' in line:
        start_idx = i
    if 'void main()' in line:
        end_idx = i

with open('menu_and_main.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines[start_idx:end_idx+300])

