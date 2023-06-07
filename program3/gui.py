import tkinter as tk
from tkinter import font, messagebox
import re

from thread_manager import ThreadManager


class GUI:
    def __init__(self) -> None:
        root_bg = '#76b5c5'
        button_bg = '#abdbe3'

        self.root = tk.Tk()
        self.root.geometry('600x425')
        self.root.config(background=root_bg)

        global_font = font.Font(self.root, 'FiraCode')

        self.output_text = tk.Text(
            self.root,
            font=global_font,
            height=15,
            width=60,
            relief='flat',
            pady=5,
            bg='#abdbe3'
        )

        self.output_text.pack(anchor='nw', expand=True, fill='both')

        self.thread_manager = ThreadManager(self.output_text)

    def run(self):
        self.root.mainloop()
