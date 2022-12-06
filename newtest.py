import threading
import time

globalTime = 6
randN = 5
inputPerm = 5

class CountdownTimer(threading.Thread):
    def __init__(self, interval, function, args=None, kwargs=None):
        threading.Thread.__init__(self)
        self.interval = interval
        self.function = function
        self.args = args if args is not None else []
        self.kwargs = kwargs if kwargs is not None else {}
        self.finished = threading.Event()
        self.started_at = None

    def cancel(self):
        self.finished.set()

    def elapsed(self):
        return time.time() - self.started_at

    def remaining(self):
        return self.interval - self.elapsed()

    def run(self):
        self.started_at = time.time()
        self.finished.wait(self.interval)
        if not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
        self.finished.set()

tmr = CountdownTimer(globalTime, print, ["Hello, World!"])
tmr.start()
time.sleep(2)
if inputPerm == randN:
    print(int(tmr.remaining()))
    tmr.cancel()