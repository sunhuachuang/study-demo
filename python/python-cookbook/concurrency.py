#! /usr/bin/python3
# 并发编程

# 2 判断线程是否已经启动

# 1 启动和停止线程 threading
import time


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


from threading import Thread

#t = Thread(target=countdown, args=(10,))
t = Thread(target=countdown, args=(5,), daemon=True)  # 后台执行

t.start()

if t.is_alive():
    print('still running')
else:
    print('completed')


class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False
        print('running stop')

    def continue_run(self):
        self._running = True

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)


c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
time.sleep(7)
c.terminate()
c.continue_run()
t.join()

# io超时循环


class IOTask:
    def terminate(self):
        self._running = False

    def run(self, sock):
        # sock is a socket
        sock.settimeout(5)        # Set timeout period
        while self._running:
            # Perform a blocking I/O operation w/ timeout
            try:
                data = sock.recv(8192)
                break
            except socket.timeout:
                continue
            # Continued processing
            pass
        # Terminated
        return
