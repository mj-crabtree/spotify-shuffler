# Spotify Playlist Shuffler

## Why
I have _zero_ data to back up this claim but I'm pretty much convinced that Spotify's shuffle feature is a bit rubbish, playing tracks it knows you'll like to hear over tracks you actually _want_ to hear (i.e. new shit) so that you keep listening for longer.

There also exists no means by which you can automatically shuffle a playlist's content in any of Spotify's apps, so I made this script.

## How
- Copy the content of a playlist to the clipboard
- Run the script
- Once it's done bin the contents of your playlist and paste into the Spotify window
- Done!

The script also creates a `.backup` file in case anything goes horribly wrong.

## Reqs.
The script uses `pyperclip`, so you'll either need to use that or whatever else you're comfortable with.

## TODO
- spotify user login
  - shuffle by playlist name from the terminal
