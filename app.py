#!flask/bin/python
from flask import Flask,jsonify
from azapi import AZlyrics

app = Flask(__name__)
az= AZlyrics('google',accuracy=0.5)


@app.route('/')
def index():
    return "App running at Beta mode!"



@app.route('/api/songs/<artist>', methods=['GET'])
def get_songs(artist):
    az.artist= artist
    songs= az.getSongs()
    return jsonify({'songs': songs})


@app.route('/api/lyric/<artist>/<song>')
def get_lyrics(artist,song):
    az.artist=artist
    az.title= song
    lyric= az.getLyrics(save=False)
    return jsonify({'Artist':az.artist,'music':az.title,'lyrics':lyric})


@app.route('/api/lyric/<song>')
def get_lyrics(song):
    az.title= song
    lyric= az.getLyrics(save=False)
    return jsonify({'Artist':az.artist,'music':az.title,'lyrics':lyric})








if __name__ == '__main__':
    app.run(debug=True)
