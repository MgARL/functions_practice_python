def name_args(**kwargs):
    for arg in kwargs.items():
        print(arg)

# name_args(a='hello', b='World')

def all_true(*args):
   return all(args)
   
# print(all_true('a',5))

def one_true(*args):
    return any(args)

# print(one_true('',5,6))

def recursive_factorial(n):
    if n <= 1:
        return n
    else:
        return n * recursive_factorial(n - 1)

# print(recursive_factorial(5))

def recursive_deduplicate(my_str,i=0):
  # if our string is empty or only has 1 thing, it's got no duplicates
  # if i is at the end of the string, no duplicates are left
  if len(my_str) <= 1 or i == len(my_str)-1:
    return my_str
  else:
    # str at current position is same as next position
    if my_str[i] == my_str[i+1]:
      return recursive_deduplicate(my_str[0:i]+my_str[i+1:],i)
    else:
      #no duplicate at current position, check next
      return recursive_deduplicate(my_str,i+1)
      
# print(recursive_deduplicate("aaaa"))
# print(recursive_deduplicate("aaba"))
# print(recursive_deduplicate("apple"))

def recursive_reverse(string):
    # base case
    if len(string) == 0:
        return string
    # recursive case
    else:
        return recursive_reverse(string[1:]) + string[0]

print(recursive_reverse('Hello!'))