import tkinter as tk
from core.ui.theme import (Theme, Font)


class SearchEntry(tk.Entry):
    def __init__(self, master, hint_text=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        if hint_text:
            self.hint = hint_text
            self.hint_visible = True

            for seq in ('<FocusIn>', '<FocusOut>'):
                self.bind(seq, self._switch_visibility_of_hint)

            self.configure(
                fg=Theme.FONT_HINT,
                bg=Theme.BACKGROUND_PRIMARY,
                font=Font.SIDEBAR_SEARCH
            )
            self.insert(0, self.hint)

    def _switch_visibility_of_hint(self, *args):
        if self.hint_visible:
            self.delete(0, tk.END)
            self.configure(
                fg=Theme.FONT_PRIMARY
            )
            self.hint_visible = False
        elif not (self.get() or self.get() == self.hint):
            self.insert(0, self.hint)
            self.configure(
                fg=Theme.FONT_HINT
            )
            self.hint_visible = True

        self.update()