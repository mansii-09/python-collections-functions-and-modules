review = """ 
Swiggy delivers food quickly.
the food is fresh and tasty.
Delivery service is fast.
"""

review = review.lower()

for char in ".,!?":
    review = review.replace(char, "")


words = review.split() 

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else :
        freq[word] = 1

print(freq)