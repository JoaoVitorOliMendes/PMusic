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
            else:
                if self.tail:
                    self.tail.next = node
                    node.previous = self.tail
            self.tail = node

    def addNextSong(self, node):
        if self.head is None:
            raise Exception("Playlist is empty")

        node.next = self.head.next
        node.previous = self.head
        self.head.next = node

        if node.next is None:
            self.tail = node
        else:
            node.next.previous = node

    def getCurrentSong(self):
        return self.index

    def hasNextSong(self):
        if self.index is None:
            return self.head
        else:
            return self.index.next

    def getNextSong(self):
        if self.index is None:
            self.index = self.head
        else:
            self.index = self.index.next

        return self.index

    def getPreviousSong(self):
        if self.index is not None:
            self.index = self.index.previous
        return self.index

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.song)
            node = node.next
        nodes.append("None")
        return nodes

