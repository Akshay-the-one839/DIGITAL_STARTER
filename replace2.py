import os

def replace_in_file(filepath):
    with open(filepath, 'rb') as f:
        content = f.read()

    old_bytes = b'''      else if (menu_number == 6) {
         handle_dryrun_delay();
      }
      else if (menu_number == 7) {
         handle_dryrun_restart();
      }
      else if (menu_number == 8) {
         handle_dryrun_trip();
      }
      else if (menu_number == 9) {
         handle_set_on_time();
      }'''
    
    # We should normalize \r\n vs \n
    old_bytes_windows = old_bytes.replace(b'\n', b'\r\n')
    
    new_bytes = b'''      else if (menu_number == 6) {
         handle_set_on_time();
      }
      else if (menu_number == 7) {
         handle_dryrun_delay();
      }
      else if (menu_number == 8) {
         handle_dryrun_restart();
      }
      else if (menu_number == 9) {
         handle_dryrun_trip();
      }'''
    new_bytes_windows = new_bytes.replace(b'\n', b'\r\n')

    if content.count(old_bytes_windows) == 0 and content.count(old_bytes) == 0:
        print("Warning: Could not find block")
    
    if old_bytes_windows in content:
        content = content.replace(old_bytes_windows, new_bytes_windows)
    elif old_bytes in content:
        content = content.replace(old_bytes, new_bytes)

    with open(filepath, 'wb') as f:
        f.write(content)
    print("Done")

replace_in_file(r'c:\3ph_Digi_starter\3ph_digi_starter.c')
