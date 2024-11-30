def full_name(first,last):
    name=f'{first} {last}'
    return name
#take perameters in orders(serial wise)
# name=full_name('Md', 'Easin')
name=full_name(last='Easin',first='Md')
print(name)

def famous_name(first,last,**addition):
    name=f'{first} {last}'
    # print(addition)
    # print(addition['title'])
    for key,value in addition.items():
        print(key,value)
    return name
name=famous_name(first='Taheri', last='ali',title="Hujur",addition="Shayok")
print(name)

def a_lot(num1,num2):
    sum=num1+num2
    multi=num1*num2
    return [sum,multi]
everything=a_lot(55,21)
print(everything)
