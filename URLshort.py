from pyshorteners import * 
from tkinter import *

smaller = Shortener()
window = Tk()
window.title("URL shortener")
window.geometry("400x210")

url = StringVar()
smol_url = StringVar()

#make the URL smol function
def make_url_smol():
    url_out = smaller.tinyurl.short(url.get())
    smol_url.set(url_out)

#header
header = Label(window,
    text="URL Shortener",
    font="verdana 16",
).pack()

header2 = Label(window,
    text="-------------------------------------",
    font="verdana 14"
).pack()

input_name = Label(window,
    text="enter URL here",
    font="verdana 12"
).pack()
#input box
name_box =  Entry(window, textvariable=url, width=50).pack(padx=8, pady=4)

convert_btn = Button(window,
    text="CONVERT", 
    fg="black",
    command=make_url_smol
).pack(padx=8, pady=4)

input_name = Label(window,
    text="short URL here",
    font="verdana 12"
).pack()
#output box
output_box =  Entry(window, textvariable=smol_url, width=50).pack(padx=8, pady=8)

#can't resize/fullscrenn
window.resizable(0, 0)
window.mainloop()