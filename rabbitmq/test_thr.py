import threading
import time


class myThread (threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Starting " + self.name)

        time.sleep(3)

        print("Exiting " + self.name)


# 创建新线程
thread1 = myThread("LINK")
thread2 = myThread("MTH")

# 开启线程
thread1.start()
thread2.start()

print("Exiting Main Thread")
