#!/usr/bin/env python3

################################################################################
##                                   README                                   ##
################################################################################
## Demo example how to create GUI programs in Python3.


################################################################################
##                                  Modules                                   ##
################################################################################
## Installation (Arch): $(pacman -S tk)
## Docs: https://docs.python.org/3/library/tkinter.html
import tkinter as tk


################################################################################
##                                 Functions                                  ##
################################################################################
def do_nothing():
    pass


def button_event():
    res = txt.get()
    lbl.configure(text=res)


## Initialize GUI window.
window = tk.Tk()

## Default window resolution.
#window.geometry("350x200")

## Window title.
#window.title("Python GUI Program")

## Initialize GUI objects..
menubar = tk.Menu(window)
submenu_1 = tk.Menu(menubar, tearoff=0)
submenu_1.add_command(label="New", command=do_nothing)
submenu_1.add_command(label="Open", command=do_nothing)
submenu_1.add_command(label="Save", command=do_nothing)
submenu_1.add_command(label="Save as...", command=do_nothing)
submenu_1.add_separator()
submenu_1.add_command(label="Exit", command=do_nothing)
submenu_2 = tk.Menu(menubar, tearoff=0)
submenu_2.add_command(label="About", command=do_nothing)
submenu_2.add_command(label="Help", command=do_nothing)
menubar.add_cascade(label="Submenu1", menu=submenu_1)
menubar.add_cascade(label="Submenu2", menu=submenu_2)
btn = tk.Button(window, text="Click Me!", command=button_event)
lbl = tk.Label(window, text="This is label.")
txt = tk.Entry(window, width=10)

## Display objects.
window.config(menu=menubar)
btn.grid(column=0, row=0)
lbl.grid(column=0, row=1)
txt.grid(column=1, row=1)

## Put everything on the display and keep looping.
window.mainloop()
