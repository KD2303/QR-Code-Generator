import customtkinter as ctk
from style import *
from PIL import Image
import pyqrcode

window = ctk.CTk()
window.title("QR Code Generator")
window.geometry("900x700")
window.iconbitmap('Logo.ico')
window.resizable(False, False)
g = 0
def generate():
    if main_x > 0.3:
        main_move()
    if side_x < 0.7:
        side_move()
    global g
    g += 1
    if g > 1:
        return
    # qr = qrcode.QRCode(
    #     version=1,
    #     error_correction=qrcode.constants.ERROR_CORRECT_L
    #     )
    # qr.add_data(text_var)
    # qr.make(fit=True)
    # img = qr.make_image(fill_color = color_var.get(), back_color = theme_var.get())
    # img.save('qr.png')
    qr= pyqrcode.create(str(text_var))
    qr.png("q2r.png", scale=8)
    global label
    label = ctk.CTkLabel(
        image_frame, 
        text = '', 
        image = ctk.CTkImage(dark_image = Image.open('q2r.png'), 
        size = (250,250)))  
    label.pack()
def main_move():
    global main_x
    main_x -= 0.01
    main_frame.place(
        relx = main_x, 
        rely = 0.5, 
        relheight = 0.8, 
        relwidth = 0.4, 
        anchor = 'center')
    if main_x > 0.3:
        window.after(10, main_move)
def side_move():
    global side_x
    side_x += 0.01
    side_frame.place(
        relx = side_x, 
        rely = 0.5, 
        relheight = 0.8, 
        relwidth = 0.4, 
        anchor = 'center')
    if side_x <= 0.7:
        window.after(10, side_move)

def clear():
    if main_x < 0.5:
        main_move_back()
    if side_x > 0.5:
        side_move_back()
    remove()
    global g
    label.pack_forget()
    g = 0
def main_move_back():
    global main_x
    main_x += 0.01
    main_frame.place(
        relx = main_x, 
        rely = 0.5, 
        relheight = 0.8, 
        relwidth = 0.4, 
        anchor = 'center')
    if main_x < 0.5:
        window.after(10, main_move_back)
def side_move_back():
    global side_x
    side_x -= 0.01
    side_frame.place(
        relx = side_x, 
        rely = 0.5, 
        relheight = 0.8, 
        relwidth = 0.4, 
        anchor = 'center')
    if side_x > 0.5:
        window.after(10, side_move_back)
def remove():
    theme_var.set('white')
    text.delete("1.0", "end")
    color.set('Black')
    
# side frame 
side_x = 0.5
side_frame = ctk.CTkFrame(window, corner_radius = 30, bg_color = 'transparent')
side_frame.place(relx = side_x, rely = 0.5, relheight = 0.8, relwidth = 0.4, anchor = 'center')

image_frame = ctk.CTkFrame(side_frame)
image_frame.place(relx = 0.5, rely = 0.45, anchor = 'center')
    

ctk.CTkLabel(side_frame, text = 'Scan it', font = ctk.CTkFont(family = FONT, size = 25)).place(relx = 0.5, rely = 0.75, anchor = 'center')

# main frame
main_x = 0.5
main_frame = ctk.CTkFrame(window, corner_radius = 30, bg_color = 'transparent')
main_frame.place(relx = main_x, rely = 0.5, relheight = 0.8, relwidth = 0.4, anchor = 'center')

# heading 
ctk.CTkLabel(
    main_frame, 
    text = 'QR Code Generator', 
    font = ctk.CTkFont(family = FONT, size = HEADING_FONTSIZE, 
    weight = 'bold'), 
    text_color = OFFWHITE
).pack(side = 'top', padx = 10, pady = 20)
    
# input box frame 
input_frame = ctk.CTkFrame(main_frame, fg_color = 'transparent')
input_frame.pack(side = 'top', expand = True, fill = 'both', padx = 10, pady = 10)

input_frame.rowconfigure((0,1,2), uniform = 'a')
input_frame.columnconfigure(0, weight = 1, uniform = 'a')
input_frame.columnconfigure(1, weight = 3, uniform = 'a')

font = ctk.CTkFont(family = FONT, size = FONTSIZE)
ctk.CTkLabel(
    input_frame, 
    text = 'Text:',
    text_color = WHITE,
    font = font
).grid(row = 0, column = 0, sticky = 'nsew', padx = 6, pady = 6)
text = ctk.CTkTextbox(input_frame, font = font, width = 7, height = 100)
text.grid(row = 0, column = 1,sticky = 'nsew', padx = 6, pady = 6)
global text_var
text_var = text.get("1.0", "end-1c")

ctk.CTkLabel(
    input_frame, 
    text = 'Color:',
    text_color = WHITE,
    font = font
).grid(row = 1, column = 0, sticky = 'nsew', padx = 6, pady = 6)

global color_var
colours = ('Black', 'Red', 'Orange', 'Yellow', 'Green', 'Blue')
color_var = ctk.StringVar(value = 'Black')
color = ctk.CTkComboBox(
    input_frame, 
    values = colours,
    font = font,
    variable = color_var)
color.grid(row = 1, column = 1)

ctk.CTkLabel(
    input_frame, 
    text = 'Theme:',
    text_color = WHITE,
    font = font
).grid(row = 2, column = 0, sticky = 'nsew', padx = 6, pady = 6)

radio_button_frame = ctk.CTkFrame(input_frame, fg_color = 'transparent')
radio_button_frame.grid(row = 2, column = 1)
radio_button_frame.rowconfigure(0, weight = 1, uniform = 'b')
radio_button_frame.columnconfigure((0,1), weight = 1, uniform = 'b')
    
global theme_var
theme_var = ctk.StringVar(value = 'white')
dark = ctk.CTkRadioButton(
    radio_button_frame, 
    text = 'Dark', 
    value = 'black', 
    variable = theme_var, 
    font = font, 
    hover_color = LIGHTGREY, 
    fg_color = GREY)
dark.grid(row = 0, column = 0, sticky = 'nsew')
light = ctk.CTkRadioButton(
    radio_button_frame, 
    text = 'Light', 
    value = 'white', 
    variable = theme_var, 
    font = font, 
    hover_color = LIGHTGREY, 
    fg_color = GREY)
light.grid(row = 0, column = 1, sticky = 'nsew')

button_frame = ctk.CTkFrame(main_frame, fg_color = 'transparent')
button_frame.pack(side = 'bottom', expand = True, fill = 'both', pady = 20, padx = 10)
button_frame.rowconfigure(0, weight = 1, uniform = 'c')
button_frame.columnconfigure((0,1), weight = 1, uniform = 'c')
    
button_font = ctk.CTkFont(family = FONT, size = BUTTON_FONTSIZE)
clear_button = ctk.CTkButton(
    button_frame, 
    text = 'Clear', 
    font = button_font, 
    fg_color = GREY, 
    hover_color = LIGHTGREY, 
    text_color = BLACK,
    command = clear)
clear_button.grid(row = 0, column = 0, sticky = 'nsew', padx = 5, pady = 5)

generate_button = ctk.CTkButton(
    button_frame, 
    text = 'Generate', 
    font = button_font, 
    fg_color = GREY, 
    hover_color = LIGHTGREY, 
    text_color = BLACK,
    command = generate)
generate_button.grid(row = 0, column = 1, sticky = 'nsew', padx = 5, pady = 5)


window.mainloop()
