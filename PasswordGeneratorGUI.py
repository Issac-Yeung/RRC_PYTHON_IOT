
 # Name: Wai Lit Yeung 
 # Program: Business Information Technology
 # Course: ADEV-3011 Internet of Things
 # Created: 07 Sept 2023
 # Updated:
 #

from guizero import App, Box, Text, TextBox, PushButton, Slider
from guizero import info
import random
#generate_password();
def generate_password():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-+'
    password_text.value = ''
    for q in range (int(password_qty.value)):
        password = ''
        for c in range(int(password_len.value)):
            password += random.choice(chars)
        password_text.value += password
    print(password_text.value)

#close_form
def close_form():
    app.destroy()

#entry point
app = App(title="Password Generator GUI", height=500)

welcome_message = Text(app, text="Password Generator", size=32, font="Times New Roman", color="blue")
blank_line1 = Text(app, text="")  # Blank line

password_qty_box = Box(app, layout="grid")
password_qty_label = Text(password_qty_box, text="Password Quantity: ", grid=[0,0])
password_qty = Slider(password_qty_box, start=1, end=20, grid=[1,0])

password_len_box = Box(app, layout="grid")
password_len_label = Text(password_len_box, text="Password Length: ", grid=[0,0])
password_len = Slider(password_len_box, start=1, end=50, grid=[1,0])

blank_line2 = Text(app, text="")  # Blank line
update_text = PushButton(app, command=generate_password, text="Generate", width=10, height=1)
blank_line3 = Text(app, text="")  # Blank line
password_text = TextBox(app, width=50, height=10, multiline=True)

blank_line4 = Text(app, text="")  # Blank line
return_status = PushButton(app, command=close_form, text="Close", width=10, height=1)

app.display()