def char_count_dict(text):
    freq  = {}

    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq

text = input("Enter a string: ")

result = char_count_dict(text)

sorted_result = dict(sorted(result.items()))

print(sorted_result)