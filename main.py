
# | Import
import customtkinter
import math
import platform
from tkinter import *


app = customtkinter.CTk()
app.title("My app")
app.minsize(640, 360)

#Base size
Base_Button_width = 140
Base_Button_height = 28
Base_Font_size = 24
Base_Padx = 10
Base_Pady = 10
Base_Window_width = 640
Base_Window_height = 320

#Zoom Factor
zoom_factor = 1
zoom_min = 1
zoom_max = 2.85

button_list = []
command_list = []
expression = ""

# | Create Display
text_display = customtkinter.StringVar()
display = customtkinter.CTkEntry(app, textvariable=text_display, placeholder_text="")
display.grid(row=0, column=0, columnspan=4, padx=Base_Padx, pady=Base_Pady, sticky="ew")

# |Button Keys
button_keys = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "x"],
    ["4", "5" , "6", "-"],
    ["1", "2", "3", "+"],
    ["0", "π", ".", "="]
]

#| Create Buttons by using loop
for row_index,list_row in enumerate(button_keys):
    for col_index, key in enumerate(list_row):
        cmd = lambda key=key: append_expression(key)
        button = customtkinter.CTkButton(app,text=key,command=cmd, width=Base_Button_width, height=Base_Button_height)
        button.grid(row=row_index+1,column=col_index, padx=Base_Padx, pady=Base_Pady)
        button_list.append(button)
        command_list.append(cmd)

# | Function

def zoom_in(event=None):
    global zoom_factor
    if zoom_factor <= zoom_max:
        zoom_factor += 0.05
        update_size()

def zoom_out(event=None):
    global zoom_factor
    if zoom_factor > zoom_min:
        zoom_factor -= 0.05
        update_size()

def update_size():
    # Update button size, font size, and window size based on zoom factor
    Button_width = int(Base_Button_width * zoom_factor)
    Button_height = int(Base_Button_height * zoom_factor)
    Font_size = int(Base_Font_size * zoom_factor)
    Window_width = int(Base_Window_width * zoom_factor)
    Window_height = int(Base_Window_height * zoom_factor)

    # Update font and button sizes
    display.configure(font=("Arial", Font_size))
    for button in button_list:
        button.configure(font=("Arial", Font_size), width=Button_width, height=Button_height)

    # Limit the window size to the minsize (640x300)
    if Window_width < Base_Window_width:
        Window_width = Base_Window_width
    if Window_height < Base_Window_height:
        Window_height = Base_Window_height

    # Apply the calculated window size
    app.geometry(f"{Window_width}x{Window_height}")

def append_expression(key):
    global expression

    if key == "AC":
        expression = ""

    elif key == "+/-":
        # Toggle negative/positive sign
        if expression.startswith("-"):
            expression = expression[1:]  # Remove the negative sign
        else:
            expression = "-" + expression  # Add the negative sign

    elif key == "=":
        try:
            # Replace symbols for division and multiplication
            expression = expression.replace("÷", "/").replace("x", "*").replace("π","math.pi")
            print(expression)
            res = str(eval(expression))  # Evaluate the expression
            expression = res  # Update expression with the result
        except Exception as e:
            expression = "Error"  # Handle errors (e.g., division by zero)
            print(expression)
           

    else:    
        expression += key

    text_display.set(expression)

# | Main

# Detect if the OS is macOS
is_mac = platform.system() == "Darwin"

# Bind the shortcuts for zoom in and zoom out
if is_mac:
    app.bind('<Command-=>', zoom_in)  # Corrected zoom in shortcut
    app.bind('<Command-minus>', zoom_out)

else:  # Windows and Linux
    app.bind('<Control-plus>', zoom_in)
    app.bind('<Control-minus>', zoom_out)


app.mainloop()

