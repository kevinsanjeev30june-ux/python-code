class Playlist :
    def __init__(self,name,songs):
        self.name = name
        self. songs = songs 

    # 1. The __len__special method
    def __len__(self):
        """Allows the use of len(playlist_object)"""
        return len(self.songs)

    # 2 . the __str__special method
    def __str__(self):
        # Controls what print(playlist_object) displays
        return f"'{self.name}' Playlist ({len(self.songs)} tracks)"
      
    # 3 .The __add__(self,new_song):  
    def __add__(self, new__song):
        """Allows us to use the '+' operator to add a song"""
        updated_songs = self.songs+ [new__song]
        return Playlist(self.name , updated_songs )
    
    def __del__(self):
        print("Object destroyed")

# ---putting it to work---
# Creating an instance of our class
my_playlist = Playlist("Chill vibes",["SongA", "Song B" , " Song C"])

# Using len() -> Triggers __len__
print(f"Playlist length: {len(my_playlist)}") # Output: 3

# Using print() -> Triggers __str__

print(my_playlist) # Output: 'Chill Vibes' Playlist (3 tracks)

# Using + operator -> Triggers __add__
my_playlist = my_playlist + "Song D"
my_playlist = my_playlist + "Song E"

print(f"New length after adding a song: {len(my_playlist)}") # Output: 4