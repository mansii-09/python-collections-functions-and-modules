usernames = ["divya", "priya", "neha"]

followers = [500, 1200, 800]

result = {}

for i in range(len(usernames)):
    result[usernames[i]] = followers[i]

print(result)