def round_views(titles, views):
    return [(title, round(view / 1000 ) * 1000) for title, view in zip(titles, views)]

titles = [
    "Python Tutorial",
    "javaScript Basics", 
    "Django Tutorial"
]

views = [125600, 234900, 1987650]

result = round_views(titles, views)

print(result)