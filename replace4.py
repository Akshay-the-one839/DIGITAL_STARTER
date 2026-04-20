filepath = r'c:\3ph_Digi_starter\3ph_digi_starter.c'
with open(filepath, 'rb') as f:
    text = f.read()

# Fix the newline issue
text = text.replace(b'\r\r\n', b'\r\n')

replacements = [
    # Change 1: menu_titles[] array
    (
        b'   "6.DRY RUN DELAY",      \r\n   "7.DRYRUN RESTART",      \r\n   "8.DRYRUN TRIP",         \r\n   "9.SET ON TIME",         ',
        b'   "6.SET ON TIME",         \r\n   "7.DRY RUN DELAY",      \r\n   "8.DRYRUN RESTART",      \r\n   "9.DRYRUN TRIP",         '
    ),
    # Change 3: handle_set_on_time()
    (b'9.SET ON TIME NRM', b'6.SET ON TIME NRM'),
    (b'9.SET ON TIME FST', b'6.SET ON TIME FST'),
    (b'9.SET ON TIME SUF', b'6.SET ON TIME SUF'),
    # Change 4: handle_dryrun_delay()
    (b'5.DRYRUN DLY NORM', b'7.DRYRUN DLY NORM'),
    (b'5.DRYRUN DLY FAST', b'7.DRYRUN DLY FAST'),
    (b'5.DRYRUN DLY SUFA', b'7.DRYRUN DLY SUFA'),
    # Change 5: handle_dryrun_restart()
    (b'6.DRYRUN RST NORM', b'8.DRYRUN RST NORM'),
    (b'6.DRYRUN RST FAST', b'8.DRYRUN RST FAST'),
    (b'6.DRYRUN RST SUFA', b'8.DRYRUN RST SUFA'),
    # Change 6: handle_dryrun_trip()
    (b'7.DRYRUN TRP NRM', b'9.DRYRUN TRP NRM'),
    (b'7.DRYRUN TRP FST', b'9.DRYRUN TRP FST')
]

for old_bytes, new_bytes in replacements:
    text = text.replace(old_bytes, new_bytes)

with open(filepath, 'wb') as f:
    f.write(text)

