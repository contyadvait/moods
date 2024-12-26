import config
import music
from flask import Flask, request, jsonify
from player import MusicPlayer
import json
import threading

app = Flask(__name__)
player = MusicPlayer()

@app.route("/")
def main():
    return "Server has started"

@app.route("/current")
def current():
    return jsonify({"song_playing": player.song_playing})

@app.route("/super")
def super():
    return json.dumps(music.organize_songs(music.get_available_songs()), indent=2, ensure_ascii=False)

@app.route("/available")
def available():
    return jsonify(music.get_available_songs())

def play_playlist(playlist_name):
    for song in config.PLAYLISTS[playlist_name]:
        song_path = f"{config.MUSIC_DIR}/{song}.mp3"
        if player.play(song_path):
            print(f"Now playing: {song}")
        else:
            print(f"Failed to play {song}")

@app.route("/play", methods=["POST"])
def play():
    data = request.json
    if "key" not in data or ("song" not in data and "playlist" not in data):
        return jsonify({"error": "Missing 'key', 'song', or 'playlist' in request"}), 400

    if data["key"] != config.KEY:
        return jsonify({"error": "Invalid key"}), 403

    if "song" in data:
        if data["song"] not in music.get_available_songs():
            print("song not found!")
            return jsonify({"error": "Song not found"}), 404

        song_path = f"{config.MUSIC_DIR}/{data['song']}.mp3"
        if player.play(song_path):
            return jsonify({"message": f"Started playing {data['song']}"})
        return jsonify({"error": "Failed to play song"}), 500

    if "playlist" in data:
        playlist_name = data["playlist"]
        if playlist_name not in config.PLAYLISTS:
            return jsonify({"error": "Playlist not found"}), 404

        # Start playing the playlist
        playlist_paths = [f"{config.MUSIC_DIR}/{song}" for song in config.PLAYLISTS[playlist_name]]
        player.play_playlist(playlist_paths)
        print("playing playlist...")
        return jsonify({"message": f"Started playing playlist {playlist_name}"})


@app.route("/playlists")
def playlists():
    return jsonify(config.PLAYLISTS)

@app.route("/pause")
def pause():
    if player.pause():
        return jsonify({"message": "Paused playback"})
    return jsonify({"error": "No song is currently playing"}), 400

@app.route("/resume")
def resume():
    if player.resume():
        return jsonify({"message": "Resumed playback"})
    return jsonify({"error": "No song is currently paused"}), 400

@app.route("/stop")
def stop():
    if player.stop():
        return jsonify({"message": "Stopped playback"})
    print("error")
    return jsonify({"error": "No song is currently playing"}), 400

if __name__ == "__main__":
    app.run(debug=True)
