team = {
    "CSK": {
        "captain": "Dhoni",
        "players": 18
    },
    "MI": {
        "captain": "Rohit",
        "players": 17
    }
}
team["GT"] = {
    "captain": "Hardik",
    "players": 16
}

# Print team names and captains
for team_name, details in team.items():
    print(team_name, ":", details["captain"])