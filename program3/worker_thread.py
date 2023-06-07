from threading import Thread, Event, Lock
from time import sleep
import tkinter as tk
from tkinter import Text


class WorkerThread(Thread):
    def __init__(self, thread_id: int, lock: Lock, output_text: Text) -> None:
        super().__init__()
        self.id = thread_id
        self.running = True
        self.lock = lock
        self.output_field = output_text

    def run(self) -> None:
        letter = 'A'
        _range = ord('Z') - ord('A')

        with self.lock:
            while self.running and letter <= 'Z':
                self.output_field.insert(tk.END, f'{letter}{self.id % 10} ')
                self.output_field.see(tk.END)
                letter = chr(ord(letter) + 1)
                sleep(1)

    def stop(self) -> None:
        self.running = False
