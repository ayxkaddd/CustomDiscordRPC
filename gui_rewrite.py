import os
import time
import json
import dbus
import tkinter
from tkinter import messagebox

import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

from DiscrodRpc import RPC

PATH = os.path.dirname(os.path.realpath(__file__))

class Gui(customtkinter.CTk):

    APP_NAME = "Custom RPC"
    WIDTH = 500
    HEIGHT = 680
    rpc = "gay"
    sincetime = time.time()

    obj = dbus.SessionBus().get_object("org.freedesktop.Notifications", "/org/freedesktop/Notifications")
    obj = dbus.Interface(obj, "org.freedesktop.Notifications")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(Gui.APP_NAME)
        self.geometry(f"{Gui.WIDTH}x{Gui.HEIGHT}")
        self.minsize(Gui.WIDTH, Gui.HEIGHT)
        self.maxsize(Gui.WIDTH, Gui.HEIGHT)
        self.resizable(False, False)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.AppFrame1 = customtkinter.CTkFrame(master=self, width=485, height=300)
        self.AppFrame1.place(x=10, y=10)

        self.IdEntry = customtkinter.CTkEntry(master=self.AppFrame1, placeholder_text="Application ID")
        self.IdEntry.place(x=20, y=20)

        self.ConnectButton = customtkinter.CTkButton(master=self.AppFrame1, command=self.Connect)
        self.ConnectButton.place(x=170, y=20)
        self.ConnectButton.configure(text="Connect")

        self.DisconnectButton = customtkinter.CTkButton(master=self.AppFrame1, command=self.Disconnect)
        self.DisconnectButton.place(x=320, y=20)
        self.DisconnectButton.configure(text="Disconnect")

        self.DetailsEntry = customtkinter.CTkEntry(master=self.AppFrame1, width=441, placeholder_text="Details")
        self.DetailsEntry.place(x=20, y=60)

        self.StateEntry = customtkinter.CTkEntry(master=self.AppFrame1, width=441, placeholder_text="State")
        self.StateEntry.place(x=20, y=100)

        self.var = tkinter.IntVar(value=1)

        self.radio1 = customtkinter.CTkRadioButton(master=self.AppFrame1, text="None", variable=self.var, value=1)
        self.radio1.place(x=150, y=140)

        self.radio2 = customtkinter.CTkRadioButton(master=self.AppFrame1, text="Since Custom RPC started", variable=self.var, value=2)
        self.radio2.place(x=150, y=170)

        self.radio3 = customtkinter.CTkRadioButton(master=self.AppFrame1, text="Local Time", variable=self.var, value=3)
        self.radio3.place(x=150, y=200)

        self.radio4 = customtkinter.CTkRadioButton(master=self.AppFrame1, text="Custom timestamp", variable=self.var, value=4)
        self.radio4.place(x=150, y=230)

        self.TimeLabel = customtkinter.CTkLabel(master=self.AppFrame1, text="Timestamp", text_font=("default_theme", 13))
        self.TimeLabel.place(x=5, y=185)

        self.TimeStampEntry = customtkinter.CTkEntry(master=self.AppFrame1, width=313, placeholder_text="7/22/2022 9:12:25 PM")
        self.TimeStampEntry.place(x=150, y=260)

        self.AppFrame2 = customtkinter.CTkFrame(master=self, width=485, height=320)
        self.AppFrame2.place(x=10, y=320)

        self.LargeImageLabel = customtkinter.CTkLabel(master=self.AppFrame2, text="Large Image", text_font=("default_theme", 11))
        self.LargeImageLabel.place(x=94, y=10)

        self.SmallImageLabel = customtkinter.CTkLabel(master=self.AppFrame2, text="Small Image", text_font=("default_theme", 11))
        self.SmallImageLabel.place(x=257, y=10)

        self.LargeImageKeyEntry = customtkinter.CTkEntry(master=self.AppFrame2, width=150, placeholder_text="Key")
        self.LargeImageKeyEntry.place(x=80, y=50)

        self.SmallImageKeyEntry = customtkinter.CTkEntry(master=self.AppFrame2, width=150, placeholder_text="Key")
        self.SmallImageKeyEntry.place(x=250, y=50)

        self.LargeImageTextEntry = customtkinter.CTkEntry(master=self.AppFrame2, width=150, placeholder_text="Text")
        self.LargeImageTextEntry.place(x=80, y=90)

        self.SmallImageTextEntry = customtkinter.CTkEntry(master=self.AppFrame2, width=150, placeholder_text="Text")
        self.SmallImageTextEntry.place(x=250, y=90)

        self.Button1Label = customtkinter.CTkLabel(master=self.AppFrame2, text="Button 1", text_font=("default_theme", 11))
        self.Button1Label.place(x=94, y=130)

        self.Button2Label = customtkinter.CTkLabel(master=self.AppFrame2, text="Button 2", text_font=("default_theme", 11))
        self.Button2Label.place(x=257, y=130)

        self.Button1LabelEntry = customtkinter.CTkEntry(master=self.AppFrame2, width=150, placeholder_text="Label")
        self.Button1URLEntry = customtkinter.CTkEntry(master=self.AppFrame2, width=150, placeholder_text="URL")

        self.Button1LabelEntry.place(x=80, y=160)
        self.Button1URLEntry.place(x=80, y=200)

        self.Button2LabelEntry = customtkinter.CTkEntry(master=self.AppFrame2, width=150, placeholder_text="Label")
        self.Button2URLEntry = customtkinter.CTkEntry(master=self.AppFrame2, width=150, placeholder_text="URL")

        self.Button2LabelEntry.place(x=250, y=160)
        self.Button2URLEntry.place(x=250, y=200)

        self.UpdateRPCButton = customtkinter.CTkButton(master=self.AppFrame2, command=self.UpdateRPC)
        self.UpdateRPCButton.place(x=170, y=260)
        self.UpdateRPCButton.configure(text="Update RPC")

        self.ConnectOrDisconnectLabel = customtkinter.CTkButton(master=self, border_width=0, fg_color=None)
        self.ConnectOrDisconnectLabel.configure(state="enable", text="Disconnected")
        self.ConnectOrDisconnectLabel.place(x=360, y=645)

        self.LoadFromConfig = customtkinter.CTkCheckBox(master=self)
        self.LoadFromConfig.configure(text="Load from config")
        self.LoadFromConfig.place(x=20, y=645)

        self.ConfigNameEntry = customtkinter.CTkEntry(master=self, width=90, placeholder_text="Config name")
        self.ConfigNameEntry.place(x=160, y=645)

        self.SaveConfigButton = customtkinter.CTkButton(master=self, command=self.SaveConfig)
        self.SaveConfigButton.configure(corner_radius=6, text="Save Config", width=50)
        self.SaveConfigButton.place(x=255, y=645)


    def Send_Notify(self, body):
        Gui.obj.Notify("", 0, "dialog-information", "Custom RPC", f"{body}", [], {"urgency": 1}, 1000)


    def Connect(self):
        try:
            appId = int(self.IdEntry.get())
            Gui.rpc = RPC(app_id=appId)
            Gui.rpc.connect()
            #    print(f"APP ID: {self.IdEntry.get()}")

            self.ConnectOrDisconnectLabel.configure(text="Connected")
            self.Send_Notify("Connected")
        except Exception as myexcept:
            print(f"{myexcept}")
            messagebox.showerror("Error", f"Wrong App ID")


    def Disconnect(self):
        try:
            Gui.rpc.clearRPC()
            self.ConnectOrDisconnectLabel.configure(state="disabled", text="Disconnected")
            self.Send_Notify("Disconnected")
        except Exception as myexcept:
            print(f"{myexcept}")


    def ButtonsCheck(self, b1label, b1URL, b2label, b2URL):
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


    def UpdateRPC(self):

        check = self.LoadFromConfig.get()
        try:
            if check == False:
                ButtonOne, ButtonTwo = self.ButtonsCheck(self.Button1LabelEntry.get(), self.Button1URLEntry.get(),
                                                         self.Button2LabelEntry.get(), self.Button2URLEntry.get())

                Gui.rpc.update(state=self.StateEntry.get(), details=self.DetailsEntry.get(), large_image=self.LargeImageKeyEntry.get(),
                        large_text=self.LargeImageTextEntry.get(), small_image=self.SmallImageKeyEntry.get(),
                        small_text=self.SmallImageTextEntry.get(), button1=ButtonOne, button2=ButtonTwo, time1=Gui.sincetime)
            else:
                config = json.load(open(f"{PATH}/configs/{self.ConfigNameEntry.get()}", "r"))
                config = config["vars"]

                appID = config["app_id"]
                Gui.rpc = RPC(app_id=appID)
                Gui.rpc.connect()

                self.ConnectOrDisconnectLabel.configure(state="disabled", text="Connected")
                self.ConnectOrDisconnectLabel.place(x=360, y=645)

                ButtonOne, ButtonTwo = self.ButtonsCheck(config["button_text_1"], config["button_url_1"],
                                                    config["button_text_2"], config["button_url_2"])

                Gui.rpc.update(state=config["state"], details=config["details"], large_image=config["large_url"],
                               large_text=config["large_text"], small_image=config["small_url"], small_text=config["small_text"],
                               button1=ButtonOne, button2=ButtonTwo, time1=Gui.sincetime)
                
            self.Send_Notify("RPC updated")
        except Exception as myexcept:
            print(f"{myexcept}")
            messagebox.showinfo("Info", "You Disconnected! Click Connect button first! (if u connected check output at terminal)")


    def SaveConfig(self):
        # get whole things

        things = {
            "vars": {
                "app_id":        self.IdEntry.get(),          
                "details":       self.DetailsEntry.get(),
                "state":         self.StateEntry.get(),
                "large_url":     self.LargeImageKeyEntry.get(),
                "large_text":    self.LargeImageTextEntry.get(),
                "small_url":     self.SmallImageKeyEntry.get(),
                "small_text":    self.SmallImageTextEntry.get(),
                "button_url_1":  self.Button1URLEntry.get(),
                "button_text_1": self.Button1LabelEntry.get(),
                "button_url_2":  self.Button2URLEntry.get(),
                "button_text_2": self.Button2LabelEntry.get(),
            }
        }

        # convert to json format and write to file

        json_vars = json.dumps(things)

        with open(f"{PATH}/{self.ConfigNameEntry.get()}", "w") as config:
            config.write(json_vars)
            config.close()

        self.Send_Notify("Config saved")


    def on_closing(self, event=0):
        self.destroy()


    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = Gui()
    app.start()
