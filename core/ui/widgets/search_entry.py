import tkinter as tk
import core


class SearchEntry(tk.Entry):
    def __init__(self, master, hint_text=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        if hint_text:
            self.hint = hint_text
            self.hint_visible = True

            for seq in ('<FocusIn>', '<FocusOut>'):
                self.bind(seq, self._switch_visibility_of_hint)

            self.configure(
                fg=core.ui.theme.FONT_HINT,
                bg=core.ui.theme.BACKGROUND_PRIMARY,
                font=core.ui.font.SIDEBAR_SEARCH
            )
            self.insert(0, self.hint)

    def _switch_visibility_of_hint(self, *args):
        if self.hint_visible:
            self.delete(0, tk.END)
            self.configure(
                fg=core.ui.theme.FONT_PRIMARY
            )
            self.hint_visible = False
        elif not (self.get() or self.get() == self.hint):
            self.insert(0, self.hint)
            self.configure(
                fg=core.ui.theme.FONT_HINT
            )
            self.hint_visible = True

        self.update()
