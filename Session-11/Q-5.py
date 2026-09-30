import random

songs = [
     "Kesariya",
    "Shape of You",
    "Believer",
    "Perfect",
    "Tum Hi Ho",
    "Apna Bana Le",
    "Chaleya",
    "Heeriye"
]

today_playlist =  random.sample(songs , 3)

print("Today's Playlist:\n",today_playlist)