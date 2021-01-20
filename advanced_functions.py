from operator import mul
'''
Today well be reviewing advanced functions/methods

- lambda [X]
- zip
- map [X]
- Counter
'''

'''
Lambda Functions

lambda input: do something with input

# Make a lambda func that adds 10 to given input
lambda x: x + 10

# Make a lambda func that adds 10 to given input IF the input is an even integer, otherwise return the integer
lambda x: (x + 10) if x % 2 == 0 else (x)
'''

def full_func(arr:list) -> list:
    'Takes in a list of integers and returns only even numbers from the list'
    res = []
    
    for i in arr:
        if i % 2 == 0:
            res.append(i)

    return res

arr_evens = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lambda_func = lambda arr: [i for i in arr if i % 2 == 0]



'''
MAP Functions

The MAP method takes in an iterable and a function to apply to the iterable. The return value of a map call is a MAP object, this usually needs to be converted to another object or type


map(function, iterable)
'''

x = '1234'

def full_map_func(char:str) -> int:
    'Takes in a string integer, converts it to int, then multiplies by 10'
    return int(char) * 10

'Apply the function to each char in the variable x, then append to a new variable'
# res = []
# for i in x:
#     res.append(full_map_func(i))
# print(res)

# map_res = list(map(full_map_func, x))
# print(map_res)

'''
Using map AND lambda, recreate the function above. So instead of using full_map_func, make a lambda instead
'''
map_lambda_res = list(map(lambda i: int(i) * 10, x))
# print(map_lambda_res)

'''
Using map AND lambda, process the given list such that every element in the list is multiplied by 5

'''

test_list = [1, 2, 3, 4, 5]
res = list(map(lambda x: x * 5, test_list))
# print(res)



'''
Zip takes in two iterables and literally ZIPs them together. The constraints of zip are based off of the shortest iterable. A zip object, MUCH like the map object needs to be converted to the desired type. For lists, it will give back a list of tuples

z_1 = 'hello'
z_2 = 'yeet'

zip_1 = zip(z_1, z_2)

'''
z_1 = 'hello'
z_2 = 'yeet'

# zip_1 = zip(z_1, z_2)
# print(list(zip_1))
# print(dict(zip(z_1, z_2)))

'''
Given two lists of PRODUCT_COUNTS and PRODUCT_PRICES, zip together the lists and multiply each of the product_counts to their prices in order to find out the estimated profit for the day if everything is sold.
'''

counts = [5, 4, 3, 2, 1]
prices = [2, 3, 4, 6, 7]

zip_profit = list(zip(counts, prices))
print(zip_profit)
res_list = []
for i, x in zip_profit:
    res_list.append(i * x)
print(sum(res_list))

zip_profit_one_line = sum(map(lambda x: mul(*x), zip(counts, prices)))
print(zip_profit_one_line)

mixed_types = ['5', 'hello', 6, True]
def process_mixed_list(lst:list) -> list:
    pass

