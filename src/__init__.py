from src.maestro import Maestro
from src.playlist import Playlist
from src.playlistNode import PlaylistNode


def cmdControl(playlist: Playlist, maestro: Maestro):
    cmd = ""
    while True:
        command = input("  ").split()

        cmd = command[0]
        command.pop(0)
        args = command

        if cmd == "play" or cmd == "p":
            if args != None:
                song = " ".join(args)
                playlist.addSong(PlaylistNode(song))
                print(f"\nAdded {song} to queue.")
            if playlist.hasNextSong():
                maestro.event.set()
        elif cmd == "now" or cmd == "n":
            crtSong = playlist.getCurrentSong()
            if crtSong:
                print("Playing Now: " + crtSong.song)
            else:
                print("Not currently playing")
        elif cmd == "queue" or cmd == "q":
            print(" Queue: \n  " + "\n  ".join(repr(playlist)))
        elif cmd == "skip" or cmd == "sk":
            crtSong = playlist.getCurrentSong()
            if crtSong:
                print("Skipping current song: " + crtSong.song)
                if maestro.process:
                    maestro.process.kill()
            else:
                print("Not currently playing")
        elif cmd != "exit" or cmd != "ex":
            print("Exiting ...")

            if maestro.process:
                maestro.process.kill()
                maestro.runThread = False
            break