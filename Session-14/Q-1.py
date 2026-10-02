cart = {}

cart.setdefault("Mansi", {})
cart["Mansi"]["Laptop"] = {
    "quantity" : 1,
    "price" : 55000
}

cart["Mansi"]["Mouse"] = {
    "quantity" : 2,
    "price" : 800
}


cart.setdefault("Khushi", {})
cart["Khushi"]["Mobile"] = {
    "quantity" : 1,
    "price" : 20000 
}

cart["Khushi"]["Headphones"] = {
    "quantity" : 1,
    "price" : 1500
}

print(cart)