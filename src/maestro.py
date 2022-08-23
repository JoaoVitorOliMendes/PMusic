import threading
import subprocess

from src.playlist import Playlist

class Maestro(threading.Thread):
    def __init__(self, playlist):
        threading.Thread.__init__(self)
        self.playlist: Playlist = playlist
        self.event = threading.Event()
        self.runThread = True
        self.process = None

    def run(self):
        while self.runThread:
            nextSong = self.playlist.getNextSong()
            while nextSong:
                song_url = subprocess.run(["youtube-dl", "-f", "140", "-g", "ytsearch1:%s" % nextSong.song], capture_output=True).stdout.decode("utf-8")[:-1]
                self.process = subprocess.Popen(args=["cvlc", "--play-and-exit", song_url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                self.process.communicate()
                nextSong = self.playlist.getNextSong()
            self.event.wait()
