filepath = r'c:\3ph_Digi_starter\3ph_digi_starter.c'
with open(filepath, 'rb') as f:
    text = f.read()

with open('old_timer.txt', 'rb') as f:
    old_timer = f.read()

# Make sure old_timer matches text
if text.find(old_timer) == -1:
    print("Error: Could not find exact match for old_timer.txt in 3ph_digi_starter.c")
    # let's try standardizing newlines just in case
    old_timer = old_timer.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')
    text = text.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')
    if text.find(old_timer) == -1:
        print("Error: Still could not find exact match. Exiting.")
        import sys
        sys.exit(1)
    else:
        print("Match found after newline standardisation")

new_timer = b'''void handle_cyclic_timer(void) {
   while (input(ENCODER_SW) == 0);
   delay_ms(50);
   
   int8 eeprom_base[] = {0x20, 0x24, 0x28, 0x2C, 0x30};
   
   char* timer_submenu[] = {
      "> TIMER 1      ",
      "> TIMER 2      ",
      "> TIMER 3      ",
      "> TIMER 4      ",
      "> TIMER 5      ",
      "> EXIT->NEXT   "
   };
   int8 total_options = 6;
   int8 sub_sel = 0;
   int8 last_sub_sel = 255;
   
   while(1) {
      // -- Sub Menu Display --
      if(sub_sel != last_sub_sel) {
         lcd_cmd(LCD_CLEAR);
         lcd_goto(1, 1);
         printf(lcd_out, "10.CYCLIC TIMER");
         lcd_goto(1, 2);
         printf(lcd_out, "%s", timer_submenu[sub_sel]);
         last_sub_sel = sub_sel;
      }
      
      // -- Encoder Rotate --
      if(input(ENCODER_A) == 0 && input(ENCODER_B) != 0) {
         delay_ms(5);
         sub_sel++;
         if(sub_sel >= total_options) sub_sel = 0;
         while(input(ENCODER_A) == 0);
         delay_ms(20);
      }
      else if(input(ENCODER_B) == 0 && input(ENCODER_A) != 0) {
         delay_ms(5);
         if(sub_sel == 0) sub_sel = total_options - 1;
         else sub_sel--;
         while(input(ENCODER_B) == 0);
         delay_ms(20);
      }
      
      // -- SW Press ? Enter selected option --
      if(input(ENCODER_SW) == 0) {
         delay_ms(20);
         if(input(ENCODER_SW) == 0) {
            while(input(ENCODER_SW) == 0);
            delay_ms(50);
            
            if(sub_sel == 5) {
               break; // Exit the loop to advance to next menu
            }
            else {
               // Timer editing block
               int8 t = sub_sel;
               
               lcd_cmd(LCD_CLEAR);
               lcd_goto(1, 1);
               printf(lcd_out, "CYCLIC TIMER %d", t+1);
               lcd_goto(1, 2);
               printf(lcd_out, "Press to ENTER");
               
               while(input(ENCODER_SW) == 1);
               delay_ms(20);
               while(input(ENCODER_SW) == 0);
               delay_ms(50);
               
               int8 base = eeprom_base[t];
               
               int8 on_hr  = read_eeprom(base + 0);
               int8 on_min = read_eeprom(base + 1);
               int8 off_hr = read_eeprom(base + 2);
               int8 off_min= read_eeprom(base + 3);
               
               if(on_hr  > 23) on_hr  = 0;
               if(on_min > 59) on_min = 0;
               if(off_hr > 23) off_hr = 0;
               if(off_min> 59) off_min= 0;
               
               int8 orig_on_hr  = on_hr;
               int8 orig_on_min = on_min;
               int8 orig_off_hr = off_hr;
               int8 orig_off_min= off_min;
               
               int8 field = 0;
               int8 last_field   = 255;
               int8 last_on_hr   = 255;
               int8 last_on_min  = 255;
               int8 last_off_hr  = 255;
               int8 last_off_min = 255;
               int1 button_pressed_flag = 0;
               
               lcd_cmd(LCD_CLEAR);
               
               while(1) {
               
                  if(field != last_field || on_hr != last_on_hr || 
                     on_min != last_on_min || off_hr != last_off_hr || 
                     off_min != last_off_min) {
                     
                     lcd_goto(1, 1);
                     printf(lcd_out, "ON :");
                     if(field == 0) printf(lcd_out, "[%02u]", on_hr);
                     else           printf(lcd_out, " %02u ", on_hr);
                     printf(lcd_out, ":");
                     if(field == 1) printf(lcd_out, "[%02u] ", on_min);
                     else           printf(lcd_out, " %02u  ", on_min);
                     
                     lcd_goto(1, 2);
                     printf(lcd_out, "OFF:");
                     if(field == 2) printf(lcd_out, "[%02u]", off_hr);
                     else           printf(lcd_out, " %02u ", off_hr);
                     printf(lcd_out, ":");
                     if(field == 3) printf(lcd_out, "[%02u] ", off_min);
                     else           printf(lcd_out, " %02u  ", off_min);
                     
                     last_field   = field;
                     last_on_hr   = on_hr;
                     last_on_min  = on_min;
                     last_off_hr  = off_hr;
                     last_off_min = off_min;
                  }
                  
                  if(input(ENCODER_A) == 0 && input(ENCODER_B) != 0) {
                     delay_ms(5);
                     switch(field) {
                        case 0: if(on_hr  < 23) on_hr++;  break;
                        case 1: if(on_min < 59) on_min++; break;
                        case 2: if(off_hr < 23) off_hr++; break;
                        case 3: if(off_min< 59) off_min++;break;
                     }
                     while(input(ENCODER_A) == 0);
                     delay_ms(30);
                  }
                  else if(input(ENCODER_B) == 0 && input(ENCODER_A) != 0) {
                     delay_ms(5);
                     switch(field) {
                        case 0: if(on_hr  > 0) on_hr--;  break;
                        case 1: if(on_min > 0) on_min--; break;
                        case 2: if(off_hr > 0) off_hr--; break;
                        case 3: if(off_min> 0) off_min--;break;
                     }
                     while(input(ENCODER_B) == 0);
                     delay_ms(30);
                  }
                  
                  if(input(KEY1) == 0) {
                     delay_ms(30);
                     field = (field + 1) % 4;
                     int8 timeout = 50;
                     while(input(KEY1) == 0 && timeout > 0) {
                        delay_ms(10);
                        timeout--;
                     }
                  }
                  
                  if(input(ENCODER_SW) == 0 && button_pressed_flag == 0) {
                     delay_ms(20);
                     if(input(ENCODER_SW) == 0) {
                        button_pressed_flag = 1;
                        
                        write_eeprom(base + 0, on_hr);
                        write_eeprom(base + 1, on_min);
                        write_eeprom(base + 2, off_hr);
                        write_eeprom(base + 3, off_min);
                        
                       lcd_cmd(LCD_CLEAR);
                        lcd_goto(1, 1);
                        printf(lcd_out, "TIMER %d SAVED!", t+1);
                        lcd_goto(1, 2);
                        printf(lcd_out, "ON%02u:%02u OF%02u:%02u",
                               on_hr, on_min, off_hr, off_min);
                        
                        // Wait for button release first (from save press)
                        while(input(ENCODER_SW) == 0);
                        delay_ms(50);
                        
                        // Stay on saved screen - wait for fresh ENTER press
                        while(input(ENCODER_SW) == 1);
                        delay_ms(20);
                        while(input(ENCODER_SW) == 0);
                        delay_ms(50);
                        
                        break;
                     }
                     else {
                        button_pressed_flag = 0;
                     }
                  }
                  
                  if(input(ENCODER_SW) != 0) {
                     button_pressed_flag = 0;
                  }
                  
                  delay_ms(1);
               }
               
               // After breaking from edit loop, force redraw of submenu
               last_sub_sel = 255; 
            }
         }
      }
   }
   
   lcd_cmd(LCD_CLEAR);
   delay_ms(100);
   advance_to_next_menu();
}'''

new_timer = new_timer.replace(b'\n', b'\r\n')
text = text.replace(old_timer, new_timer)

with open(filepath, 'wb') as f:
    f.write(text)

print("Replacement Complete")
