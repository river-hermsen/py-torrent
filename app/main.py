import customtkinter
from tkinter import Tk


class Dashboard(Tk):
    def __init__(self):
        super().__init__()

        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure((0, 1), weight=1)

        self.frame = customtkinter.CTkFrame(self, width=200, bg_color="gray25")
        self.frame.place(x=0, y=0, relheight=1)
        self.frame.grid_propagate(False)

        self.text = customtkinter.CTkLabel(
            self, text="Hello ,World!", font=("roboto", 40)
        )
        self.text.place(x=200, y=50)
        self.text.lower()


class NavBar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.label = customtkinter.CTkLabel(
            self, text="Hello, World!", font=("roboto", 40)
        )
        self.label.grid(row=0, column=0, sticky="nsew")


app = customtkinter.CTk()


app = Dashboard()
app.title("my app")
app.geometry("1920x1080")

app.mainloop()
