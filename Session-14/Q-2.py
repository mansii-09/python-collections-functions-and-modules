def add_song_to_playlist(playlists, user, playlist_name, song_title, artist):

    playlists.setdefault(user, {})
    playlists[user].setdefault(playlist_name, [])

    playlists[user][playlist_name].append({
        "title" : song_title,
        "artist" : artist
    })

playlists = {}

add_song_to_playlist(playlists, "Mansi", "Favorite Songs", "Shape of You", "Ed Sheeran")
add_song_to_playlist(playlists, "Mansi", "Favorite Songs","perfect", "Ed Sheeran")
add_song_to_playlist(playlists, "khushi", "chill", "Night Changes", "One Direction")

print(playlists)