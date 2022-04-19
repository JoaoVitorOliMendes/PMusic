import queue
import subprocess
import threading

from pmusic import PMusic

def maestro():
    cmd = ""
    while True:
        command = input("  ").split()

        cmd = command[0]
        command.pop(0)
        args = command

        if cmd == "play" or cmd == "p":
            if args != None:
                song = " ".join(args)
                songList.append(song)
                song_queue.put(song)
                print(f"\nAdded {song} to queue.")
            if song_queue.qsize() == 1:
                pmusicInst.event.set()
        elif cmd == "now" or cmd == "n":
            print("Playing Now: " + songList[-1])
        elif cmd == "queue" or cmd == "q":
            print(" Queue: \n  " + "\n  ".join(songList))
        elif cmd == "skip" or cmd == "sk":
            print("Skipping current song: " + songList[-1])
            pmusicInst.process.kill()
        elif cmd != "exit" or cmd != "ex":
            print("Exiting ...")

            song_queue.mutex.acquire()
            song_queue.queue.clear()
            song_queue.all_tasks_done.notify_all()
            song_queue.unfinished_tasks = 0
            song_queue.mutex.release()
            
            pmusicInst.process.kill()
            pmusicInst.runThread = False
            break

songList = []
song_queue = queue.Queue()

pmusicInst = PMusic(song_queue)

def main():

    pmusicInst.start()

    maestro()

    pmusicInst.join()
    song_queue.join()

if __name__ == "__main__":
    main()
