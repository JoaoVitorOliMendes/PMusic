class PlaylistNode:
    def __init__(self, song=None):
        self.song = song
        self.next: PlaylistNode | None = None
        self.previous: PlaylistNode | None = None

    def __repr__(self):
        nextSong = "Null"
        previousSong = "Null"
        if self.next:
                nextSong = str(self.next.song)
        if self.previous:
            previousSong = str(self.previous.song)
        return "Song: " + str(self.song) + "; Next: " + nextSong + "; Previous: " + previousSong

