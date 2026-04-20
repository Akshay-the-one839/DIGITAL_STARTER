filepath = r'c:\3ph_Digi_starter\3ph_digi_starter.c'
with open(filepath, 'rb') as f:
    text = f.read()

# Change 1: handle_menu wrap
old_menu_start = b'''void handle_menu(void) {
   if (in_menu_selection) {
      handle_menu_navigation();
   }
   
   if (!in_menu_selection && prog == 1) {'''

new_menu_start = b'''void handle_menu(void) {
   while (prog == 1) {
      if (in_menu_selection) {
         handle_menu_navigation();
      }
      
      if (!in_menu_selection && prog == 1) {'''

# Change 2: handle_menu end
old_menu_end = b'''      else if (menu_number == 14) {
         handle_polarization_index_menu(); 
      }
   }
}'''

new_menu_end = b'''      else if (menu_number == 14) {
         handle_polarization_index_menu(); 
      }
   }
   }
}'''

# Change 3: main() block
old_main_block = b'''        else if (prog == 1) {
           disable_interrupts(int_AD);
           disable_interrupts(int_TIMER1);  
           lcd_cmd(LCD_CLEAR); 
           handle_menu();
           lcd_cmd(LCD_CLEAR); 
           enable_interrupts(int_AD);
           enable_interrupts(int_TIMER1);
           enable_interrupts(GLOBAL);
        }'''

new_main_block = b'''        else if (prog == 1) {
           disable_interrupts(int_AD);
           disable_interrupts(int_TIMER1);
           lcd_cmd(LCD_CLEAR);
           handle_menu();
           enable_interrupts(int_AD);
           enable_interrupts(int_TIMER1);
           enable_interrupts(GLOBAL);
        }'''


# Normalize line endings to avoid failure if they are just \n
def apply_replace(full_text, old_seg, new_seg):
    if old_seg in full_text:
        return full_text.replace(old_seg, new_seg)
    
    old_seg_n = old_seg.replace(b'\r\n', b'\n')
    new_seg_n = new_seg.replace(b'\r\n', b'\n')
    if old_seg_n in full_text:
        return full_text.replace(old_seg_n, new_seg_n)
        
    old_seg_rn = old_seg_n.replace(b'\n', b'\r\n')
    new_seg_rn = new_seg_n.replace(b'\n', b'\r\n')
    if old_seg_rn in full_text:
        return full_text.replace(old_seg_rn, new_seg_rn)
    
    print(f"Warning: Segment not found: {old_seg[:50]}")
    return full_text

text = apply_replace(text, old_menu_start, new_menu_start)
text = apply_replace(text, old_menu_end, new_menu_end)
text = apply_replace(text, old_main_block, new_main_block)

with open(filepath, 'wb') as f:
    f.write(text)

print("Replacement logic complete.")
