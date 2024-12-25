# Moods - the custom music player
Have you ever felt down one day and wanted the least amount of friction in your room to start playing music? well, introduing moods, you best friend for this!

It runs on a couple basic GET and POST requests to help play music directly on your PC. There is also a mobile app (refer to the mobile_apps folder for code) which is basically a set of simple buttons

It's very adaptable, and picks up all the MP3s you have of your favourite songs!

## Demo

## How do I make this my own?
The only things you will need to setup are the non-Python based dependencies for the requirements (check requirements.txt) and `config.py`. Here is an example `config.py` for you to use in creating your own one

```python
MUSIC_DIR = "/Users/conytadvait/Music" 
# Without the / at the end else it won't work!

KEY = "soote" 
# For security reasons, so your friends can't just randomly POST to it!

# Not required but up to you!
PLAYLISTS = {"wind down": ["C418 - Minecraft.mp3", 
                           "C418 - Sweden.mp3", 
                           "C418 - Mice On Venus.mp3",
                           "C418 - Subwoofer Lullaby.mp3",
                           "C418 - Wet Hands.mp3",
                           "C418 - Haggstrom.mp3"],
            "relax": ["BoyWithUke - I Wish.mp3",
                      "BoyWithUke - Animal Crackers.mp3",
                      "BoyWithUke - Nightmare.mp3",
                      "BoyWithUke - Blurry Nights.mp3"]}
```

Finally, if you wanna set up the mobile app to your own server, just change the server and password in settings!

(screenshot)