calls = (12,5,0,20,7,3,15)

call_list = list(calls)

call_list = [time for time in call_list if time >= 5]

calls = tuple(call_list)

print(calls)