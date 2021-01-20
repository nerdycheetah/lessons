'''
Recursion Practice 10/17/2020

Example: Let's make a function that takes in a number and recursively adds to the total until the number reaches 1
'''

def recursive_total(n:int) -> int:
    if n == 1:
        return n
    else:
        print(f'n is currently: {n}')
        return recursive_total(n - 1) + n

print(recursive_total(10))