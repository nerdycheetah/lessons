def count_vowels(string1:str) -> int:
    """Takes in a string and returns the number of vowels"""
    count = 0
    iterable = 'aeiou'
    for i in string1:
        if i in iterable:
            count += 1
    return count
