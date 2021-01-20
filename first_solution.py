def even_num_counterpart(list1:list):
    """Takes in a list of numbers, finds the even
    numbers in the list, and prints out their word
    representation"""
    num_word_dict = {
        2:'two',
        4:'four',
        6:'six',
        8:'eight'
    }
    for i in list1:
        if i % 2 == 0:
            print(num_word_dict[i])

even_num_counterpart([1,2,3,4,5,6,7,8])
