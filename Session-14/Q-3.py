ipl = {}

ipl.setdefault("CSK", {})
ipl["CSK"]["Dhoni"] = 45
ipl["CSK"]["Rutura"] = 72
ipl["CSK"]["Jadeja"] = 35

ipl.setdefault("MI", {})
ipl["MI"]["Rohit"] = 65
ipl["MI"]["Surya"] = 80
ipl["MI"]["Hardik"] = 40

print(ipl)

print("Surya scored: ", ipl["MI"]["Surya"])