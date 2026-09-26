teams = ["CSK", "MI", "RCB", "GT"]
points = [12, 8, 14, 10]

result = dict(zip(teams, points))

for team,point in result.items():
    if point > 10:
        print(team, point)