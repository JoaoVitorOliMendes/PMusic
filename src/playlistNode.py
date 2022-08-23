class PlaylistNode:
    def __init__(self, song):
        self.song = song
        self.next: PlaylistNode | None = None
        self.previous: PlaylistNode | None = None
