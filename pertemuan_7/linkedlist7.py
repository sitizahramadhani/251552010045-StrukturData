class songNode:
    def __init__(self,title):
        self.title= title
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None
    
    def add_song(self,title):
        new_song = songNode(title)
        if not self.head:
            self.head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_song
        print(f"Lagu '{title}' ditambahkan ke playlist.")

    def  show_playlist(self):
        current = self.head
        if not current:
            print(f"-{current.title}")
            current = current.next

    def play_all(self):
        current = self.head
        if not current:
            print("Tidak ada lagu untuk diputar.")
            return
        print("Memutar semua lagu.")
        while current:
            print(f"Memutar:{current.title}")
            current = current.next
        
Playlist = Playlist()

Playlist.add_song("Lagu A-Aku")
Playlist.add_song("Lagu B-Bersamamu")
Playlist.add_song("Lagu C-kita")

print()
Playlist.show_playlist

print()
Playlist.play_all()
