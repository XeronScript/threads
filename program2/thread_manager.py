from worker_thread import WorkerThread
from threading import Lock
from tkinter import Text


class ThreadManager:
    def __init__(self) -> None:
        self.threads = []
        self.lock = Lock()

    def start_threads(self, thread_num: list[int], output_text: Text) -> None:
        for thread_id in thread_num:
            thread = WorkerThread(thread_id, self.lock, output_text)
            thread.setDaemon(True)
            thread.start()
            self.threads.append(thread)

    def stop_threads(self, thread_num: list[int]) -> None:
        for thread in self.threads:
            if thread.id in thread_num:
                thread.stop()
