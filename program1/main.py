from threading import Thread


def my_print():
    print('Hello World!!')


if __name__ == '__main__':
    thread = Thread(target=my_print)
    thread.start()
    thread.join()
