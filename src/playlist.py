from src.playlistNode import PlaylistNode


class Playlist:
    def __init__(self):
        self.head: PlaylistNode | None = None
        self.tail: PlaylistNode | None = None
        self.index: PlaylistNode | None = None


    def addSong(self, node):
        if node:
            if self.head is None:
                self.head = node
                self.index = PlaylistNode(None)
                self.index.next = self.head
            else:
                if self.tail:
                    self.tail.next = node
                    node.previous = self.tail
            self.tail = node
            if self.index is None:
                self.index = self.tail
                print(str(self.index) + "PLAYLIST" + str(self.tail))

    def addNextSong(self, node):
        if self.head is None:
            raise Exception("Playlist is empty")

        node.next = self.head.next
        node.previous = self.head
        self.head.next = node

        if node.next is None:
            self.tail = node
            if self.index is None:
                 self.index = self.tail
        else:
            node.next.previous = node

    def getCurrentSong(self):
        return self.index

    def hasNextSong(self):
        if self.index:
            print(repr(self.index.next))
            return self.index.next
        return self.index

    def getNextSong(self):
        if self.index:
            self.index = self.index.next
        return self.index

    def getPreviousSong(self):
        if self.index is not None:
            self.index = self.index.previous
        return self.index

    def getPlaylist(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.song)
            node = node.next
        nodes.append("None")
        return nodes

