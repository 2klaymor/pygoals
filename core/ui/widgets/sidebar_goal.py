import tkinter as tk


class SideBarGoal(tk.Label):
    def __init__(self, master, name):
        super().__init__(master)

        self.name_var = tk.StringVar(
            value=name
        )

        self.configure(
            textvariable=self.name_var
        )
