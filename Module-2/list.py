#index   0  1  2  3  4  5  6  7   8   
numbers=[45,20,30,40,50,60,70,100,20]

#revers  -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# index
print(numbers[3],numbers[-3])
#list(start:end)
print(numbers[2:6])#starts with the start index and stops before the end index

#list(start:end:step)
print(numbers[1:7:2])

print(numbers[7:2:-1])

print(numbers[4:])
print(numbers[::-1])