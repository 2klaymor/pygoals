import tkinter as tk
from core.theme import Theme


class SearchEntry(tk.Entry):
    def __init__(self, master, hint_text=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        if hint_text:
            self.hint_text = hint_text
            self.hint_visible = True

            for seq in ('<FocusIn>', '<FocusOut>'):
                self.bind(seq, self._switch_visibility_of_hint)

            self.configure(fg=Theme.TEXT_HINT)
            self.insert(0, self.hint_text)

    def _switch_visibility_of_hint(self, *args):
        if self.hint_visible:
            self.delete(0, tk.END)
            self.configure(
                fg=Theme.TEXT
            )
            self.hint_visible = False
        else:
            self.insert(0, self.hint_text)
            self.configure(
                fg=Theme.TEXT_HINT
            )
            self.hint_visible = True

        self.update()