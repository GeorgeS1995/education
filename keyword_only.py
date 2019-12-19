def total (initial = 5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    return count

print(total(10, 10, extra_number = 50))
print(total(10, 10))