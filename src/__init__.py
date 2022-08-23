from src.maestro import Maestro
from src.playlist import Playlist
from src.playlistNode import PlaylistNode

def cmdControl():
    playlist = Playlist()
    maestro = Maestro(playlist)

    maestro.start()

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
            if crtSong and crtSong.song:
                print("Playing Now: " + crtSong.song)
            else:
                print("Not currently playing")
        elif cmd == "queue" or cmd == "q":
            print(" Queue: \n  " + "\n  ".join(playlist.getPlaylist()))
        elif cmd == "skip" or cmd == "sk":
            crtSong = playlist.getCurrentSong()
            if crtSong and crtSong.song:
                print("Skipping current song: " + crtSong.song)
                if maestro.process:
                    maestro.process.kill()
            else:
                print("Not currently playing")
        elif cmd == "loop-queue" or cmd == "lq":
            #TODO: loop all songs
            pass
        elif cmd == "loop-current" or cmd == "lc":
            #TODO: loop current song
            pass
        elif cmd == "pnext":
            if args != None:
                song = " ".join(args)
                playlist.addNextSong(PlaylistNode(song))
                print(f"\nNext song is going to be: {song}")
            if playlist.hasNextSong():
                maestro.event.set()
        elif cmd != "exit" or cmd != "ex":
            print("Exiting ...")

            if maestro.process:
                maestro.process.kill()
                maestro.runThread = False
            break
    maestro.join()
