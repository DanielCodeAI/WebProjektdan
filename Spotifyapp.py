import json
import os
import time
import random
import string
##############################################
class Song:
    def __init__(self, name, artist, album, genre, duration):
        self.artist = artist
        self.album = album
        self.duration = duration
        self.genre = genre
        self.name = name
    
    def __str__(self):
        return f"{self.name} by {self.artist} - Album: {self.album}, Genre: {self.genre}, Duration: {self.duration}"

    def to_dict(self):
        return {
            "name": self.name,
            "artist": self.artist,
            "album": self.album,
            "genre": self.genre,
            "duration": self.duration
        }

    @staticmethod 
    def from_dict(data):
        return Song(data['name'], data['artist'], data['album'], data['genre'], data['duration'])
    
    def __lt__(self, other):
        return self.name < other.name
    
    def __le__(self, other):
        return self.name <= other.name
    
    def __gt__(self, other):
        return self.name > other.name

    def __eq__(self, other):
        return self.name == other.name

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self):
        return f"Playlist: {self.name}, Songs: {len(self.songs)}"

    def to_dict(self):
        return {
            "name": self.name,
            "songs": [song.to_dict() for song in self.songs]
        }

    @staticmethod 
    def from_dict(data):
        playlist = Playlist(data['name'])
        playlist.songs = [Song.from_dict(song_data) for song_data in data['songs']]
        return playlist

class MusicApp:
    def __init__(self, data_file='music_data.json'):
        self.data_file = data_file
        self.songs = []
        self.playlists = []
        self.load_data()

        if not self.songs:
            print("No songs found in the database. Generating 1000 random songs...")
            self.songs = self.generate_random_songs(1000)
            self.save_data()

    def generate_random_string(self, min_length=3, max_length=10):
        length = random.randint(min_length, max_length)
        return ''.join(random.choices(string.ascii_lowercase, k=length)).capitalize()

    def generate_random_duration(self):
        minutes = random.randint(2, 5)
        seconds = random.randint(0, 59)
        return f"{minutes}:{seconds:02d}"

    def generate_random_songs(self, num_songs):
        songs = []
        for _ in range(num_songs):
            name = self.generate_random_string()
            artist = self.generate_random_string()
            album = self.generate_random_string()
            genre = self.generate_random_string()
            duration = self.generate_random_duration()
            song = Song(name, artist, album, genre, duration)
            songs.append(song)
        return songs

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.songs = [Song.from_dict(song_data) for song_data in data.get('songs', [])]
                self.playlists = [Playlist.from_dict(pl_data) for pl_data in data.get('playlists', [])]
            print("Data loaded successfully.")
        else:
            print("No data file found. Starting with an empty database.")

    def save_data(self):
        data = {
            "songs": [song.to_dict() for song in self.songs],
            "playlists": [playlist.to_dict() for playlist in self.playlists]
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully.")

    def add_song(self):
        name = input("Enter song name: ")
        artist = input("Enter artist name: ")
        album = input("Enter album name: ")
        genre = input("Enter genre: ")
        duration = input("Enter duration (mm:ss): ")
        song = Song(name, artist, album, genre, duration)
        self.songs.append(song)
        print(f"Added song: {song}")

    def create_playlist(self):
        name = input("Enter playlist name: ")
        playlist = Playlist(name)
        self.playlists.append(playlist)
        print(f"Created playlist: {playlist.name}")

    def add_song_to_playlist(self):
        playlist_name = input("Enter the name of the playlist: ")
        playlist = next((pl for pl in self.playlists if pl.name.lower() == playlist_name.lower()), None)
        if not playlist:
            print(f"Playlist '{playlist_name}' not found.")
            return

        song_name = input("Enter the name of the song to add: ")
        song = next((s for s in self.songs if s.name.lower() == song_name.lower()), None)
        if not song:
            print(f"Song '{song_name}' not found.")
            return

        playlist.add_song(song)
        print(f"Added song '{song.name}' to playlist '{playlist.name}'.")

    def linear_search(self, song_input=None):
        if song_input is None:
            song_input = input("Enter the song name to search: ").lower()
        start_time = time.time()
        for index, song in enumerate(self.songs):
            if song.name.lower() == song_input:
                print(f"Found song '{song.name}' at index {index}. Search took {time.time() - start_time:.6f} seconds.")
                return index
        print(f"Song '{song_input}' not found. Search took {time.time() - start_time:.6f} seconds.")
        return -1

    def binary_search(self, arr=None, song_input=None):
        if arr is None:
            arr = self.songs
        if song_input is None:
            song_input = input("Enter the song name to search: ").lower()
        arr = self.quicksort(arr)
        left, right = 0, len(arr) - 1
        start_time = time.time()
        while left <= right:
            mid = (left + right) // 2
            if arr[mid].name.lower() == song_input:
                print(f"Found song '{arr[mid].name}' at index {mid}. Search took {time.time() - start_time:.6f} seconds.")
                return mid
            elif arr[mid].name.lower() < song_input:
                left = mid + 1
            else:
                right = mid - 1
        print(f"Song '{song_input}' not found. Search took {time.time() - start_time:.6f} seconds.")
        return -1

 


    def quicksort(self, arr=None):
        if arr is None:
            arr = self.songs
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quicksort(left) + middle + self.quicksort(right)

    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def search_songs_with_algorithms(self):
        print("1. Linear Search")
        print("2. Binary Search")
        option = input("Choose a search algorithm: ")
        
        if option == '1':
            self.linear_search()
        elif option == '2':
            sorted_songs = self.quicksort(self.songs)
            self.binary_search(arr=sorted_songs)
        else:
            print("Invalid option selected.")


    def sort_songs_with_algorithms(self):
        print("1. Quicksort")
        print("2. Bubble sort")
        print("3. Merge Sort")
        option = input("Choose your sorting algorithm: ")
        
        start_time = time.time()  # Start the timer

        if option == '1':
            self.songs = self.quicksort(self.songs)
            print(f"Quicksort: Duration: {time.time() - start_time:.6f} seconds")
        elif option == '2':
            self.songs = self.bubble_sort(self.songs)
            print(f"Bubble Sort: Duration: {time.time() - start_time:.6f} seconds")
        elif option == '3':
            self.songs = self.merge_sort(self.songs)
            print(f"Merge Sort: Duration: {time.time() - start_time:.6f} seconds")
        else:
            print("Invalid option selected.")

  

    def display_all_songs(self):
        if not self.songs:
            print("No songs available.")
        else:
            for song in self.songs:
                print(song)

    def display_playlists(self):
        if not self.playlists:
            print("No playlists available.")
        else:
            for playlist in self.playlists:
                print(playlist)
                for song in playlist.songs:
                    print(f"  - {song}")

    def main_menu(self):
        while True:
            print("\n--- Music App ---")
            print("1. Add New Song")
            print("2. Create Playlist")
            print("3. Add Song to Playlist")
            print("4. Search Songs")
            print("5. Sort Songs")
            print("6. Display All Songs")
            print("7. Display Playlists")
            print("8. Save and Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_song()
            elif choice == '2':
                self.create_playlist()
            elif choice == '3':
                self.add_song_to_playlist()
            elif choice == '4':
                self.search_songs_with_algorithms()
            elif choice == '5':
                self.sort_songs_with_algorithms()
            elif choice == '6':
                self.display_all_songs()
            elif choice == '7':
                self.display_playlists()
            elif choice == '8':
                self.save_data()
                print("Exiting the app.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = MusicApp()
    app.main_menu()
