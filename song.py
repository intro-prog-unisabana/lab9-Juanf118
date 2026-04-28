# Write your code here!
class Song:
    def __init__(self, name, artist, length):
        self.name = name
        self.artist = artist
        self.length = float(length)
    def get_length_in_seconds(self):
        return self.length * 60

my_song = Song("Bohemian Rhapsody", "Queen", 5.55)
print(my_song.get_length_in_seconds())