# Write your code here!

class Song:
    def __init__(self, name, artist, length):
        self.name = name
        self.artist = artist
        self.length = float(length)
    def get_length_in_seconds(self):
        return self.length * 60
    def __str__(self):
        return f"{self.name} by {self.artist} ({self.length})"
    def __repr__(self) -> str:
        return f"Song(name={self.name!r}, artist={self.artist!r}, length={self.length!r})"
    
if __name__ == "__main__":
    my_song = Song("tv off", "Kendrick Lamar", 3.7)
    print(my_song)
    print(my_song.get_length_in_seconds())