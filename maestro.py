import threading

class Maestro(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global songList
        global isPlaying


        while True:
            query = input("Query: ")
            songList.append(query)
            if not isPlaying:
                print("Playing %s" % query)
            print(songList)
