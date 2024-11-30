numbers=input()
rev=str(int(numbers[::-1]))
print(rev)
if(numbers[::1])==(numbers[::-1]):
    print("YES")
else: print("NO")