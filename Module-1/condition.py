#int,not,not in,is not,and,or
a=7
a=a+5
a+=a
if a>10:
    print("Greater than 10")
elif a>12:
    print("Greater than 12")
else:
    print("Smaller than 10 and 12")

boss=True
if boss is True:
    print("Taratari kaaj koro")
if boss is not True:
    print("Have some chill")
#Nasted conditions
target=153
rain=True
coin="Head"
if rain==False:
    print("We will play")
    if coin=="Head":
        print("We will bat")
    else:
        print("We will ball")
        if target>150:
            print("We will win")
        else:
            print("We will not win")
else:
    print("We won't play")