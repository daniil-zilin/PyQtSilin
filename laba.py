daniil_list = [11, 'daniil', 14, 22, 'ulsu', 96, 'alex']

evenNumbers = []

for item in daniil_list:
    if type(item) is int:
        if item % 2 == 0:
            evenNumbers.append(str(item))

print(" ".join(evenNumbers))