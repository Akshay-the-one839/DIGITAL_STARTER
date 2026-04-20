import re

filepath = r'c:\3ph_Digi_starter\3ph_digi_starter.c'
with open(filepath, 'rb') as f:
    text = f.read().decode('utf-8', errors='ignore')

# Change 2
pattern = r'(else if \(menu_number == 6\) \{\s*)handle_dryrun_delay\(\);(\s*\})\s*(else if \(menu_number == 7\) \{\s*)handle_dryrun_restart\(\);(\s*\})\s*(else if \(menu_number == 8\) \{\s*)handle_dryrun_trip\(\);(\s*\})\s*(else if \(menu_number == 9\) \{\s*)handle_set_on_time\(\);'
repl = r'\1handle_set_on_time();\2\3handle_dryrun_delay();\4\5handle_dryrun_restart();\6\7handle_dryrun_trip();'

new_text, count = re.subn(pattern, repl, text)
print(f"Change 2 replacements: {count}")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_text)

