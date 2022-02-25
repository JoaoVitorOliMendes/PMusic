import threading
import time

class PMusic(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.paused = False
        self.pauseCondition = threading.Condition(threading.Lock())

    def run(self):
        while True:
            with self.pauseCondition:
                while self.paused:
                    self.pauseCondition.wait()
                print("started")
            time.sleep(5)

    def pause(self):
        self.paused = True
        self.pauseCondition.acquire()

    def resume(self):
        self.paused = False
        self.pauseCondition.notify()
        self.pauseCondition.release()

