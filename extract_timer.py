filepath = r'c:\3ph_Digi_starter\3ph_digi_starter.c'
with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if 'void handle_cyclic_timer(void)' in line:
        start_idx = i
    if start_idx != -1 and 'void handle_auto_restart_mode()' in line:
        # found the next function, search upwards for }
        for j in range(i-1, start_idx, -1):
            if lines[j].strip() == '}':
                end_idx = j
                break
        break

with open('old_timer.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines[start_idx:end_idx+1])

