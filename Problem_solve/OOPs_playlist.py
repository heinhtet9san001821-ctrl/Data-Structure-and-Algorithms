class Playlist:
    def __init__(self, name):
        self.name=name
        self.songs=[]

    def show_playlist_name(self):
        return self.name

    def add_song_to_list(self,song):
        print(f"The {song}  is add to {self.name} playlist.")
        return self.songs.append(song)    

    def remove_song_from_list(self,song):
        print(f"The song {song}  is removed from {self.name} playlist.")
        return self.songs.remove(song)

    def show_all_song(self):
        return self.songs

