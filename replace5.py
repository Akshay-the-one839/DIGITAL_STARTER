filepath = r'c:\3ph_Digi_starter\3ph_digi_starter.c'
with open(filepath, 'rb') as f:
    text = f.read()

# Fix the formatting for Change 2
old = b'''      }else if (menu_number == 7) {
         handle_dryrun_delay();
      }else if (menu_number == 8) {
         handle_dryrun_restart();
      }else if (menu_number == 9) {
         handle_dryrun_trip();        
      }'''

new = b'''      }
      else if (menu_number == 7) {
         handle_dryrun_delay();
      }
      else if (menu_number == 8) {
         handle_dryrun_restart();
      }
      else if (menu_number == 9) {
         handle_dryrun_trip();        
      }'''

text = text.replace(old, new)
with open(filepath, 'wb') as f:
    f.write(text)

