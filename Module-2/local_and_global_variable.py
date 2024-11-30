#global variable
balance=5000
def buy_things(item,price):
    # balance=3000(local variable)
    global balance
    print(f'previous balance value',balance)
    balance=balance-price
    print(f'Balance after buying{item}',balance)
buy_things('sunglass',2000)
