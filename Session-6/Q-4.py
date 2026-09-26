titles = ["KGF" , "3 Idiots", "Dangal"]
genres = ["Action","Comedy", "Drama"]
rating = [8.5,8.4,8.3]

result = []

for title,genre,rating in zip(titles,genres,rating):
    movie = {
        "Title" : title,
        "Genre" : genre,
        "Rating": rating
    }

    result.append(movie)

print(result)