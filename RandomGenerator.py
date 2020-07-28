import unittest
import random
import spotipy
import flask
from flask import render_template
from flask import Flask
app = Flask(__name__)

rand = random.Random()

def random_number_generator(num1, num2):    
    if not num1.isnumeric():
        print("Computer says no")
        return 0
    if not num2.isnumeric():
        print("Computer says no")
        return 0

    output = random.randint(int(num1), int(num2))
    print("Random number is: " + str(output))
    return int(output)

@app.route('/')
def open_page():
    return render_template("Index.html")

@app.route('/<name>', methods=["GET", "POST"])
def get_spotify_artist_details(name):

    spotify = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyClientCredentials(client_id="1bfcea2c51bf4242baa6a1bb008381df", client_secret="fa54c12f61fd488c977ec5b87cff5cdb"))
    results = spotify.search(q="artist: " + name, type="artist")
    items = results["artists"]["items"]
    albums = spotify.search(q="artist: " + name, type="album")
    album_list = albums["albums"]["items"]

    if len(items) > 0:
        artist = items[0]
        album = album_list[0]
        artist_uri = artist['uri']
        album_uri = album['uri']
        tracks = spotify.artist_top_tracks(artist_uri)
        print("#######################")
        artist_name = artist['name']
        artist_image = artist['images'][0]['url']
        artist_album = album['name']
        random_artists = ['Queen', 'Michael Jackson', 'Madonna', 'The Beatles', 'Guns n Roses', 'Lady Gaga', 'Areosmith', 'Nirvana', 'Ed Sheeran','Elton John']
        
        print("\nArtist Name & Image: " + artist['name'], artist['images'][1]['url'])
        print("\nArtist URI: " + artist_uri)
        
        print("\nArtist Album: " + album['name'] + ", type of album: " + album['type'])
        print("\nTop tracks include: ")        
        for track in tracks['tracks'][:3]:
            print(track['name'])
            if str(track['preview_url']) == "None":
                print("No Preview Available")
            else:
                print(" " + str(track['preview_url']))
            print()     
        print("#######################")
        return render_template("artist.html", name=name, artist_uri=artist_uri, artist_image=artist_image, artist_album=artist_album)

if __name__ == "__main__":
        app.run()
