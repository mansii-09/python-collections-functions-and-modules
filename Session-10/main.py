from playlist import add_song, remove_song, display_playlist

playlist = []

# Add 3 songs
add_song("Kesariya", playlist)
add_song("Shape of You", playlist)
add_song("Believer", playlist)

print("Playlist after adding songs:")
display_playlist(playlist)

# Remove Shape of You
remove_song("Shape of You", playlist)

print("\nPlaylist after removing Shape of You:")
display_playlist(playlist)