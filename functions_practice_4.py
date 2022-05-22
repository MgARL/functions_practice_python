from unittest import result


def max_num(x, y, z):
    n_arr = [x,y,z]
    max_n = x
    for n in n_arr:
        if n > max_n:
            max_n = n
    return max_n
print(max_num(-200,-100,-70))

def mult_list(list):
    result = 1
    for n in list:        
       result = result * n
    return result
print(mult_list([3,2,6]))

def rev_string(string):
    # base case
    if len(string) == 0:
        return string
    # recursive case
    else:
        return rev_string(string[1:]) + string[0]
print(rev_string('Hello'))

def num_within(x,y,z):
    # It checks if the first Number is between the other two
    return( x >= y and x <= z) or ( x <= y and x >=z)
print(num_within(5, 3,7 ))

def pascal(n):
    #Loop for rows
    for my_row in range(1,n+1):#we add one to the end because it stops at the number before it is selected
        #other loop to format
        for j in range(0, n-1+1):
            print(' ', end='\n')
        col = 1 #the number to be printed
        #Second inner loop for columns
        for cols in range(1, my_row+1):
            print(' ',col, sep='', end='')
            col = col * (my_row - cols) // cols
    print()

pascal(5)
