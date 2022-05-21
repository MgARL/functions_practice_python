def hello():
    print('Hello, Welcome')

def pack(a,b,c):
    return [a,b,c]

def eat_lunch(list):
    if len(list) > 0:
        print(f'First I eat {list[0]}')
        for index, item in enumerate(list):
            if index > 0:
                print(f'Next, I eat {item}')
    else:
        print('My lunchbox is empty')

hello()
my_list = pack('Ham', 'Bread', 'Juice')
eat_lunch(my_list)
    


