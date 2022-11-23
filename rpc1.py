from pypresence import Presence

class RPC:

    def __init__(self, app_id, RPC=0):

        self.app_id = app_id
        self.RPC = RPC


    def update(self, state, details, large_image, large_text, small_image, small_text, button1, button2, time1=None):
        print("DEBUG:", state, details, large_image, large_text,
              small_image, small_text, button1, button2)

        if not state:
            state = None
        if not details:
            details = None
        if not large_image:
            large_image = None
        if not large_text:
            large_text = None
        if not small_image:
            small_image = None
        if not small_text:
            small_text = None
        if not button1:
            button1 = None
        if not button2:
            button2 = None

        if button1 and button2:
            okButtonOne = button1
            okButtonTwo = button2
            bruhbuttons = [
                okButtonOne,
                okButtonTwo
            ]
            print(f"1: {bruhbuttons=}")
        elif button1:
            okButtonOne = button1
            bruhbuttons = [
                okButtonOne
            ]
            print(f"2: {bruhbuttons=}")
        elif button2:
            okButtonTwo = button_2
            bruhbuttons = [
                okButtonTwo
            ]
            print(f"2: {bruhbuttons=}")
        else:
            bruhbuttons = None
            print(f"4: {bruhbuttons=}")


        self.RPC.update(
            state=f"{state}",
            details=f"{details}",
            start=time1,
            buttons=bruhbuttons,
            large_image=f"{large_image}",
            large_text=f"{large_text}",
            small_image=f"{small_image}",
            small_text=f"{small_text}"
        )


    def connect(self):
        self.RPC = Presence(f"{self.app_id}")
        self.RPC.connect()
        print("connected")


    def clearRPC(self):
        # self.connect()
        self.RPC.close()
        print("disconnected")
