from worker_thread import WorkerThread
from threading import Lock
from tkinter import Text


class ThreadManager:
    def __init__(self, output_text_field: Text) -> None:
        lock = Lock()
        self.threads = [WorkerThread(i, lock, output_text_field) for i in range(1, 11)]
        for thread in self.threads:
            thread.setDaemon(True)
            thread.start()

    def stop_threads(self, thread_num: list[int]) -> None:
        for thread in self.threads:
            if thread.id in thread_num:
                thread.stop()
