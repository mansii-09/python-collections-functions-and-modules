text = "The food is tasty and the delivery is fast"

text = text.lower()

for char in ".,!?":
    text = text.replace(char, "")

words = text.split()

stopwords = ["the", "and", "in", "of", "a", "to", "is"]

freq = {}

for word in words:
    if word not in stopwords:
        if word in freq:
            freq[word] += 1
        else :
            freq[word] = 1

print(freq)