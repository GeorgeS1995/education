CountOf3 = 0
CountOf5 = 0

for i in range(1, 100):
    if i % 3 == 0:
        CountOf3 += 1
    elif i % 5 == 0:
        CountOf5 += 1
total = CountOf3 + CountOf5
print(total)