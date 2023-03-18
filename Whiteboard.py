import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor
import pyautogui
root = tk.Tk()
from PIL import ImageGrab
from tkinter.filedialog import *


def paint(event):
    # draw a line on the canvas
    x1, y1 = event.x, event.y
    x2, y2 = (event.x+10), (event.y+10)
    canvas.create_line(x1, y1, x2, y2, fill=color.get(), width=scale.get())


def clear_canvas():
    canvas.delete("all")
def erase():
    new_color = '#FFFFFF'
    print(new_color)
    if new_color:
        color.set(new_color)


def change_color():
    # change color
    new_color = askcolor(color.get())[1]
    print(new_color)

    if new_color:
        color.set(new_color)


def screenshot():
    screen_shot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    if save_path:
        screen_shot = ImageGrab.grab()
        screen_shot.save(save_path+'_screenshot.png')


root.title("Whiteboard Application")
# create a canvas
canvas = tk.Canvas(root, bg='white', width=800, height=800)
canvas.pack(fill='both', expand=True)
canvas.bind('<B1-Motion>', paint)
# create a frame
control_frame = ttk.Frame(root)
control_frame.pack(side='bottom', fill='x')
# color selector
color_label = ttk.Label(control_frame, text='Color : ', font=('Stencil 20'))
color_label.pack(side='left', padx=5, pady=5)
color = tk.StringVar()
color.set('black')
color_button = tk.Button(control_frame, text='Choose Color', font=('Lucida 20 bold'), bg='lightblue', command=change_color)
color_button.pack(side='left', padx=5, pady=5, ipadx=10, ipady=10)
# brush size
scale_label = ttk.Label(control_frame, text='Brush Size', font=('Stencil 20'))
scale_label.pack(side='left', padx=15, pady=15)
scale = tk.Scale(control_frame, from_=1, to=100, orient='horizontal', borderwidth=10, font=20)
scale.pack(side='left', padx=5, pady=(30, 40), ipadx = 30)
erase_button = tk.Button(control_frame, text='Eraser', font=('Lucida 25 bold'), bg='lightblue', command=erase)
clear_button = tk.Button(control_frame, text='Clear', font=('Lucida 25 bold'), bg='lightblue', command=clear_canvas)
screenshot_button = tk.Button(control_frame, text='Screenshot', font=('Lucida 25 bold'), bg='lightblue', command=screenshot)
clear_button.pack(side='right', padx=5, pady=5, ipadx=20, ipady=20)
erase_button.pack(side='right', padx=5, pady=5, ipadx=20, ipady=20)
screenshot_button.pack(side='right', padx=5, pady=5, ipadx=20, ipady=20)


root.mainloop()
