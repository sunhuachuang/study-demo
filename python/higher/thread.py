from threading import Thread, currentThread, activeCount, RLock
from time import sleep


def test(s):
    print("ident: ", currentThread().ident)
    print("count: ", activeCount())
    print(s)


test(1)

Thread(target=test, args=("hello", )).start()


class MyThread(Thread):
    def __init__(self, name, *args):
        super(MyThread, self).__init__(name=name)
        self.data = args

    def run(self):
        print(self.name, self.data)


MyThread("sun", [1, 2, 3, 4]).start()


def show():
    print("_thread_ start...")
    sleep(3)
    print("_thread_ exit...")


def run():
    t = Thread(target=show)
    t.start()
    t.join(2)

    print(t.isAlive())
    t.join()
    print("over")


run()


lock = RLock()


def show2(i):
    with lock:
        print(currentThread().name, i)
        sleep(0.1)


def test2():
    with lock:
        for i in range(5):
            show2(i)


for i in range(2):
    Thread(target=test2).start()
