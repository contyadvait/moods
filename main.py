import config
import music
from flask import Flask, request, jsonify
from player import MusicPlayer
import json

app = Flask(__name__)
player = MusicPlayer()


app.route("/")
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

@app.route("/play", methods=["POST"])
def play():
    data = request.json
    print(music.get_available_songs())
    if "key" not in data or "song" not in data:
        return jsonify({"error": "Missing 'key' or 'song' in request"}), 400

    if data["song"] not in music.get_available_songs():
        return jsonify({"error": "Song not found"}), 404

    if data["key"] != config.KEY:
        return jsonify({"error": "Invalid key"}), 403

    song_path = f"{config.MUSIC_DIR}/{data['song']}.mp3"


    if player.play(song_path):
        return jsonify({"message": f"Started playing {data['song']}"})
    return jsonify({"error": "Failed to play song"}), 500

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
    return jsonify({"error": "No song is currently playing"}), 400

if __name__ == "__main__":
    app.run(debug=True)