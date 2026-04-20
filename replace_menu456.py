filepath = r'c:\3ph_Digi_starter\3ph_digi_starter.c'
with open(filepath, 'rb') as f:
    text = f.read()

replacements = [
    # Change 1: menu_titles[] array
    (
        b'   "4.STAR DELTA DLY",\r\n   "5.VOLT SETTING",    \r\n   "6.SET ON TIME",         ',
        b'   "4.SET ON TIME",         \r\n   "5.STAR DELTA DLY",\r\n   "6.VOLT SETTING",    '
    ),
    # Change 2: handle_menu() order
    (
        b'      else if (menu_number == 4) {\r\n         handle_star_delta_delay();\r\n      }\r\n      else if (menu_number == 5) {\r\n         handle_voltage_setting();\r\n      }\r\n      else if (menu_number == 6) {\r\n         handle_set_on_time();\r\n      }',
        b'      else if (menu_number == 4) {\r\n         handle_set_on_time();\r\n      }\r\n      else if (menu_number == 5) {\r\n         handle_star_delta_delay();\r\n      }\r\n      else if (menu_number == 6) {\r\n         handle_voltage_setting();\r\n      }'
    ),
    # Change 3: handle_star_delta_delay()
    (b'4.STAR DELT NRM', b'5.STAR DELT NRM'),
    (b'4.STAR DELT FST', b'5.STAR DELT FST'),
    # Change 4: handle_voltage_setting()
    (b'5.VOLT SETTING  ', b'6.VOLT SETTING  '),
    # Change 5: handle_set_on_time() (Was previously updated from 9 -> 6, now 6 -> 4)
    (b'6.SET ON TIME NRM', b'4.SET ON TIME NRM'),
    (b'6.SET ON TIME FST', b'4.SET ON TIME FST'),
    (b'6.SET ON TIME SUF', b'4.SET ON TIME SUF')
]

for old_bytes, new_bytes in replacements:
    text = text.replace(old_bytes, new_bytes)

with open(filepath, 'wb') as f:
    f.write(text)

