import tkinter as tk

import core.shared.theme


class CheckBox(tk.Button):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.checked = '✔️'
        self.unchecked = '⭕'

        self._state = False
        self.funcs = [self.switch_state]

        self.var = tk.StringVar(value=self.unchecked)
        self.configure(
            textvariable=self.var,
            fg=core.shared.theme.TOGGLE_FG_UNCHECKED,
            bg=core.shared.theme.TOGGLE_BG_UNCHECKED
        )
        self.bind(
            '<Button-1>',
            self.call_funcs
        )

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.check_state()

    def switch_state(self):
        if self._state:
            self.var.set(self.unchecked)
            self.configure(
                fg=core.shared.theme.TOGGLE_FG_UNCHECKED,
                bg=core.shared.theme.TOGGLE_BG_UNCHECKED
            )
            self._state = False
        else:
            self.var.set(self.checked)
            self.configure(
                fg=core.shared.theme.TOGGLE_FG_CHECKED,
                bg=core.shared.theme.TOGGLE_BG_CHECKED
            )
            self._state = True

    def check_state(self):
        if not self._state:
            self.var.set(self.unchecked)
            self.configure(
                fg=core.shared.theme.TOGGLE_FG_UNCHECKED,
                bg=core.shared.theme.TOGGLE_BG_UNCHECKED
            )
        else:
            self.var.set(self.checked)
            self.configure(
                fg=core.shared.theme.TOGGLE_FG_CHECKED,
                bg=core.shared.theme.TOGGLE_BG_CHECKED
            )

    def call_funcs(self, *args):
        for func in self.funcs:
            func()

    def add_binding(self, func):
        self.funcs.append(func)
