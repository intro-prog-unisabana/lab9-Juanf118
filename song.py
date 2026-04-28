# Write your code here!
class Song:
    def __init__(self, name, artist, length):
        self.name = name
        self.artist = artist
        self.length = float(length)
    def get_length_in_seconds(self):
        return self.length * 60
    def __str__(self):
        return f"{self.name} by {self.artist} ({self.get_length_in_seconds()} seconds)"
if __name__ == "__main__":
    name = input("Enter the song name: ")
    artist = input("Enter the artist's name: ")
    length = input("Enter the length of the song in minutes: ")
    my_song = Song(name, artist, length)
    print(my_song.__str__())