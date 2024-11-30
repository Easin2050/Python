numbers=[45,87,65,85,14,26,61]
odds=[]
for num in numbers:
    if num%2==1 and num%2==0:
        odds.append(num)

print(odds)

odds_numbers=[num for num in numbers if num%2==1]
print(odds_numbers)

players=['sakib','mosfiq','musta']
ages=[38,37,32]
age_com=[]
for player in players:
    print('Players:',player)
    for age in ages:
        print(player,age)
        age_com.append([player,age])
print(age_com)

age_com2=[[player,age] for player in players for age in ages]
print(age_com2)