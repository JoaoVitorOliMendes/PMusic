import time
import subprocess
from sys import stderr, stdout
import threading


def pmusic():
    global isPlaying
    global songList
    global songIndex
    global event

    while True:
        while isPlaying:
            song = songList[songIndex]
            print("\nNow playing: %s" % song)
            song_url = subprocess.run(["youtube-dl", "-f", "140", "-g", "ytsearch1:%s" % song], capture_output=True).stdout.decode("utf-8")[:-1]
            subprocess.run(["cvlc", "--play-and-exit", song_url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if len(songList) > (songIndex + 1):
                songIndex += 1
            else:
                isPlaying = False
        event.wait()

def maestro():
    global isPlaying
    global songList
    global songIndex
    global event

    while True:
        command = input(" ").split()
        cmd = command[0]
        command.pop(0)
        args = command
        if cmd == "play" or cmd == "p":
            if args != None:
                songList.append(" ".join(args))
            if not isPlaying:
                isPlaying = True
                event.set()
        elif cmd == "queue" or cmd == "q":
            print("Queue: " + ", ".join(songList))
        elif cmd == "skip" or cmd == "sk":
            print("TODO")


event = threading.Event()

p = threading.Thread(target=pmusic)
m = threading.Thread(target=maestro)

isPlaying = False
songList = []
songIndex = 0

def main():

    m.start()
    p.start()

    m.join()
    p.join()


if __name__ == "__main__":
    main()
