# "pyinstaller --noconfirm --onefile --windowed --icon "D:/Medal/icon.png" --add-data "C:/Users/Користувач/AppData/Local/Programs/Python/Python310/Lib/site-packages/customtkinter;customtkinter/"  gui.py"

# gui

import tkinter
from tkinter import messagebox
import customtkinter

# time lol

import time

# work with discord RPC

from rpc1 import RPC

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.iconbitmap("D:/Download/icon.ico")
app.geometry("500x680")
app.resizable(width=False, height=False)
app.title("Custom Discord RPC")


rpc = None
sincetime = None

def Connect():
    global rpc, sincetime
    sincetime = time.time()
    try:
        appId = int(IdEntry.get())
        rpc = RPC(app_id=appId)
        rpc.connect()
        print(f"APP ID: {IdEntry.get()}")

        ConnectOrDisconnectLabel.configure(state="disabled", text="Connected")
        ConnectOrDisconnectLabel.place(x=360, y=645)
    except Exception as myexcept:
        print(f"{myexcept}")
        messagebox.showerror("Error", f"{myexcept}")


def Disconnect():
    global rpc
    try:
        rpc.clearRPC()
        ConnectOrDisconnectLabel.configure(state="disabled", text="Disconnected")
        ConnectOrDisconnectLabel.place(x=360, y=645)
    except Exception as myexcept:
        print(f"{myexcept}")


def ButtonsCheck():
    b1label = Button1LabelEntry.get()
    b1URL = Button1URLEntry.get()
    b2label = Button2LabelEntry.get()
    b2URL = Button2URLEntry.get()

    if not b1label:
        ButtonOne = ""
    else:
        ButtonOne = {
            "label": f"{b1label}",
            "url": f"{b1URL}"
        }

    if not b2label:
        ButtonTwo = ""
    else:
        ButtonTwo = {
            "label": f"{b2label}",
            "url": f"{b2URL}"
        }
    return ButtonOne, ButtonTwo


def UpdateRPC():
    global rpc, sincetime
    try:
        ButtonOne, ButtonTwo = ButtonsCheck()
        rpc.update(state=StateEntry.get(), details=DetailsEntry.get(), large_image=LargeImageKeyEntry.get(),
                    large_text=LargeImageTextEntry.get(), small_image=SmallImageKeyEntry.get(),
                    small_text=SmallImageTextEntry.get(), button1=ButtonOne, button2=ButtonTwo, time1=sincetime)
    except Exception as myexcept:
        print(f"{myexcept}")
        messagebox.showinfo("Info", "You Disconnected! Click Connect button first!")


AppFrame1 = customtkinter.CTkFrame(master=app, width=485, height=300)
AppFrame1.place(x=10, y=10)

IdEntry = customtkinter.CTkEntry(master=AppFrame1, placeholder_text="Application ID")
IdEntry.place(x=20, y=20)

ConnectButton = customtkinter.CTkButton(master=AppFrame1, command=Connect)
ConnectButton.place(x=170, y=20)
ConnectButton.configure(state='enable', text="Connect")

DisconnectButton = customtkinter.CTkButton(master=AppFrame1, command=Disconnect)
DisconnectButton.place(x=320, y=20)
DisconnectButton.configure(state='enable', text="Disconnect")

DetailsEntry = customtkinter.CTkEntry(master=AppFrame1, width=441, placeholder_text="Details")
DetailsEntry.place(x=20, y=60)
StateEntry = customtkinter.CTkEntry(master=AppFrame1, width=441, placeholder_text="State")
StateEntry.place(x=20, y=100)

var = tkinter.IntVar(value=1)

radio1 = customtkinter.CTkRadioButton(master=AppFrame1, text="None", variable=var, value=1)
radio1.place(x=150, y=140)

radio2 = customtkinter.CTkRadioButton(master=AppFrame1, text="Since Custom RPC started", variable=var, value=2)
radio2.place(x=150, y=170)

radio3 = customtkinter.CTkRadioButton(master=AppFrame1, text="Local Time", variable=var, value=3)
radio3.place(x=150, y=200)

radio4 = customtkinter.CTkRadioButton(master=AppFrame1, text="Custom timestamp", variable=var, value=4)
radio4.place(x=150, y=230)

TimeLabel = customtkinter.CTkLabel(master=AppFrame1, text="Timestamp", text_font=("default_theme", 13))
TimeLabel.place(x=5, y=185)

TimeStampEntry = customtkinter.CTkEntry(master=AppFrame1, width=313, placeholder_text="7/22/2022 9:12:25 PM")
TimeStampEntry.place(x=150, y=260)

AppFrame2 = customtkinter.CTkFrame(master=app, width=485, height=320)
AppFrame2.place(x=10, y=320)

LargeImageLabel = customtkinter.CTkLabel(master=AppFrame2, text="Large Image", text_font=("default_theme", 11))
LargeImageLabel.place(x=80, y=10)

SmallImageLabel = customtkinter.CTkLabel(master=AppFrame2, text="Small Image", text_font=("default_theme", 11))
SmallImageLabel.place(x=240, y=10)

LargeImageKeyEntry = customtkinter.CTkEntry(master=AppFrame2, width=150, placeholder_text="Key")
LargeImageKeyEntry.place(x=80, y=50)

SmallImageKeyEntry = customtkinter.CTkEntry(master=AppFrame2, width=150, placeholder_text="Key")
SmallImageKeyEntry.place(x=250, y=50)

LargeImageTextEntry = customtkinter.CTkEntry(master=AppFrame2, width=150, placeholder_text="Text")
LargeImageTextEntry.place(x=80, y=90)

SmallImageTextEntry = customtkinter.CTkEntry(master=AppFrame2, width=150, placeholder_text="Text")
SmallImageTextEntry.place(x=250, y=90)

Button1Label = customtkinter.CTkLabel(master=AppFrame2, text="Button 1", text_font=("default_theme", 11))
Button1Label.place(x=80, y=130)

Button2Label = customtkinter.CTkLabel(master=AppFrame2, text="Button 2", text_font=("default_theme", 11))
Button2Label.place(x=240, y=130)

Button1LabelEntry = customtkinter.CTkEntry(master=AppFrame2, width=150, placeholder_text="Label")
Button1URLEntry = customtkinter.CTkEntry(master=AppFrame2, width=150, placeholder_text="URL")

Button1LabelEntry.place(x=80, y=160)
Button1URLEntry.place(x=80, y=200)

Button2LabelEntry = customtkinter.CTkEntry(master=AppFrame2, width=150, placeholder_text="Label")
Button2URLEntry = customtkinter.CTkEntry(master=AppFrame2, width=150, placeholder_text="URL")

Button2LabelEntry.place(x=250, y=160)
Button2URLEntry.place(x=250, y=200)

UpdateRPCButton = customtkinter.CTkButton(master=AppFrame2, command=UpdateRPC)
UpdateRPCButton.place(x=170, y=280)
UpdateRPCButton.configure(state='enable', text="Update RPC")

ConnectOrDisconnectLabel = customtkinter.CTkButton(master=app, border_width=0, fg_color=None)
ConnectOrDisconnectLabel.configure(state="enable", text="Disconnected")
ConnectOrDisconnectLabel.place(x=360, y=645)

app.mainloop()