from ast import Return, alias


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

# hello()
# my_list = pack('Ham', 'Bread', 'Juice')
# eat_lunch(my_list)


def arb_args(*args):
    for arg in args :
        print(arg)

# arb_args(1,5,6,9,3)

def inner_func(int_a,int_b):
    def multiply():
        return int_a * int_b
    def divide ():
        return int_a / int_b
    
    print(multiply() + divide())
inner_func(2,2)

def lunch_lady(name, lunch_pref='Mystery Meat'):
    print(f'hello {name}, your lunch will be {lunch_pref}')
# lunch_lady('Miguel')

def sum_n_product(x, y):
    return x + y, x * y
# print(sum_n_product(4, 4))

alias_arb_args = arb_args

# alias_arb_args(1,5,6,9,3)

def arb_mean(*args):
    sum = 0
    for arg in args:
        sum += arg
    print(sum / len(args))

# arb_mean(1,2,3,4)

def arb_longest_string(*args):
    longest = ''
    for arg in args:
        if len(arg) > len(longest):
            longest = arg
    print(longest)
# arb_longest_string('hello', 'world','python','javascript')

def get_max_str(*args):
    return max(args, key=len)

print(get_max_str('hello', 'world','python','javascript'))
