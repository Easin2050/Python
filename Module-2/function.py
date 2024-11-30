def double_it(num):
    result=num*2
    print(result)
    return result
double_it(8)

def sum(num1,num2):
    result2=num1+num2
    return result2

result3=sum(44,39)
print("Total value:",result3)
final=double_it(result3(90))
print(final)

#args
def all_sum(*numbers):
    print(numbers)
    sum=0
    for num in numbers:
        print(num)
        sum+=num
    return sum

total=all_sum(45,46,89,11,81)
print("All sum:",total)