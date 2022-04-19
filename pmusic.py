import curses
import threading
import subprocess

class PMusic(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.song_queue = queue
        self.event = threading.Event()
        self.process = None
        self.runThread = True

    def run(self):

        while self.runThread:
            while self.song_queue.qsize() > 0:
                song = self.song_queue.get()
                song_url = subprocess.run(["youtube-dl", "-f", "140", "-g", "ytsearch1:%s" % song], capture_output=True).stdout.decode("utf-8")[:-1]
                self.process = subprocess.Popen(args=["cvlc", "--play-and-exit", song_url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                self.process.communicate()
                self.song_queue.task_done()
            self.event.wait()
