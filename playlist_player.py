import vlc
from utilities import takeCommand, speak

def play_playlist(playlist_path):
    """
    Play songs from a playlist file.

    Args:
        playlist_path (str): Path to the playlist file.

    Returns:
        None
    """
    try:
        player = vlc.MediaPlayer()
        with open(playlist_path, "r") as file:
            songs = file.readlines()
            for song in songs:
                song_path = song.strip()
                player.set_mrl(song_path)
                player.play()
                speak(f"Now playing: {song_path}")
                speak("Please say 'Next' to play the next song.")
                takeCommand()  # Wait for user command
    except Exception as e:
        speak("Error playing playlist")
        print("Error playing playlist:", e)

def pause_playlist(player):
    """
    Pause the currently playing song in the playlist.

    Args:
        player (vlc.MediaPlayer): VLC media player instance.

    Returns:
        None
    """
    if player is not None:
        player.pause()
        speak("Playlist paused.")

def resume_playlist(player):
    """
    Resume the paused playlist.

    Args:
        player (vlc.MediaPlayer): VLC media player instance.

    Returns:
        None
    """
    if player is not None:
        player.play()
        speak("Playlist resumed.")

def stop_playlist(player):
    """
    Stop playing the playlist.

    Args:
        player (vlc.MediaPlayer): VLC media player instance.

    Returns:
        None
    """
    if player is not None:
        player.stop()
        speak("Playlist stopped.")

def main():
    """
    Main function to demonstrate the usage of playlist functions.
    """
    player = None
    while True:
        command = takeCommand().lower()
        if "play" in command:
            playlist_path = "playlist.txt"
            play_playlist(playlist_path)
        elif "pause" in command:
            pause_playlist(player)
        elif "resume" in command:
            resume_playlist(player)
        elif "stop" in command:
            stop_playlist(player)
        elif "exit" in command:
            if player is not None:
                stop_playlist(player)
            break
        else:
            speak("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
