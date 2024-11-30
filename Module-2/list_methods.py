numbers=[12,13,16,17]
numbers.append(56)
print(numbers)
numbers.insert(2,81)
print(numbers)
if 7 in numbers:
    numbers.remove(7)
print(numbers)
last=numbers.pop()
print(last, numbers)
index=numbers.index(12)
print(index)
numbers.sort()
print(numbers)