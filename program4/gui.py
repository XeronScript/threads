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
        self.label = tk.Label(
            self.root,
            font=global_font,
            text='Podaj numery wątków, którymi chcesz sterować.',
            bg=root_bg
        )
        self.input_text = tk.Entry(
            self.root,
            bd=3,
            font=global_font,
            bg='#abdbe3',
            relief='flat',
            width=30,
            justify='center',

        )
        self.stop_button = tk.Button(
            self.root,
            text="Stop",
            command=self.on_stop_click,
            font=global_font,
            width=15,
            relief='flat',
            borderwidth=3,
            bg=button_bg
        )

        self.output_text.pack(anchor='nw', expand=True, fill='x')
        self.label.pack(anchor='n')
        self.input_text.pack(pady=2)
        self.stop_button.pack(pady=5)

        self.thread_manager = ThreadManager(self.output_text)

    def parse_input(self) -> list[int]:
        """
        Parses user input and converts it into a list of integers representing thread numbers.

        The user input cna be in the following formats:
        - Single number: '5' -> [5]
        - Number range: '1-5' -> [1, 5]
        - Combination of number ranges and individual numbers: '1-3, 6' -> [1, 3, 6]
        :return: list[int]: A list of integers representing the thread number range extracted from the user input
        """
        user_input = self.input_text.get()
        split_user_input = re.split('[ ,-]', user_input)
        filter_user_input = filter(lambda x: x != '', split_user_input)
        map_user_input = map(int, filter_user_input)
        list_user_input = list(map_user_input)
        return list_user_input if len(list_user_input) > 1 else list_user_input * 2

    def on_stop_click(self) -> None:
        """
        Callback function triggered when the stop button is clicked.

        This function retrieves user input from a text field, handles potential exceptions, and stops
        individual worker threads.

        :raises ValueError: If the user input is invalid, specifically if the thread number range is incorrect.
        :return: None
        """
        try:
            parsed_input = self.parse_input()
            if not self.is_valid_input(parsed_input):
                raise ValueError
            if len(parsed_input) == 0:
                return

            threads_range = [*range(parsed_input[0], parsed_input[1] + 1)]
            self.thread_manager.stop_threads(threads_range)

        except ValueError:
            messagebox.showwarning('Warning', 'Incorrect thread number range')

    def is_valid_input(self, parsed_input: list[int]) -> bool:
        if len(parsed_input) > 2:
            return False

        if parsed_input[0] > parsed_input[1]:
            return False

        return True

    def run(self):
        self.root.mainloop()
