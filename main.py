import queue
import curses
import subprocess
import threading
from curses import COLOR_BLACK

from pmusic import PMusic

#def pmusic():
#    global process
#
#    while True:
#        while song_queue.qsize() > 0:
#            song = song_queue.get()
#            upperwindow.addstr(f"\nNow playing: {song}")
#            upperwindow.refresh()
#            song_url = subprocess.run(["youtube-dl", "-f", "140", "-g", "ytsearch1:%s" % song], capture_output=True).stdout.decode("utf-8")[:-1]
#            process = subprocess.Popen(args=["cvlc", "--play-and-exit", song_url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#            process.communicate()
#            song_queue.task_done()
#        event.wait()

def maestro():
    cmd = ""
    while cmd != "exit" or cmd != "ex":
        lowerwindow.addstr(" ")
        command = lowerwindow.getstr().decode("utf-8").split()
        cmd = command[0]
        command.pop(0)
        args = command
        if cmd == "play" or cmd == "p":
            if args != None:
                song = " ".join(args)
                songList.append(song)
                song_queue.put(song)
                upperwindow.addstr(f"\nAdded {song} to queue.")
                upperwindow.refresh()
            if song_queue.qsize() == 1:
                pmusic.event.set()
        elif cmd == "queue" or cmd == "q":
            lowerwindow.addstr(" Queue: " + ", ".join(songList))
        elif cmd == "clear" or cmd == "cls":
            upperwindow.clear()
            upperwindow.refresh()
        elif cmd == "skip" or cmd == "sk":
            lowerwindow.addstr("Skipping current song: " + songList[-1])
            process.kill()
        lowerwindow.clear()
        lowerwindow.refresh()

scr = curses.initscr()
scr.keypad(True)

lines = curses.LINES
columns = curses.COLS

upperwindow = scr.subwin(lines - 2, columns, 0, 0)
lowerwindow = scr.subwin(lines - 1, 0)

#event = threading.Event()

songList = []
song_queue = queue.Queue()

process = None

pmusic = PMusic(song_queue, upperwindow)

def main():

    #p = threading.Thread(target=pmusic)

    #p.start()

    maestro()

    #p.join()
    song_queue.join()

    scr.keypad(False)
    curses.echo()
    curses.endwin()


if __name__ == "__main__":
    main()
