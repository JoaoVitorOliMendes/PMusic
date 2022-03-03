import curses
import threading
import subprocess

class PMusic(threading.Thread):
    def __init__(self, queue, scr):
        threading.Thread.__init__(self)
        self.song_queue = queue
        self.event = threading.Event()
        self.stdscr = scr

    def run(self):
        global process

        while True:
            self.stdscr.addstr("====================")
            while self.song_queue.qsize() > 0:
                song = self.song_queue.get()
                self.stdscr.addstr(f"\nNow playing: {song}")
                self.stdscr.refresh()
                song_url = subprocess.run(["youtube-dl", "-f", "140", "-g", "ytsearch1:%s" % song], capture_output=True).stdout.decode("utf-8")[:-1]
                process = subprocess.Popen(args=["cvlc", "--play-and-exit", song_url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                process.communicate()
                self.song_queue.task_done()
            self.event.wait()
