import math
def binary_search(my_list,item):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = math.floor((low+high)/2)
        guess = my_list[mid]
        print('low',low,'high',high,'mid',mid,'guess',guess)
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return 'none'
list_ = [1,3,5,7,9]

print(binary_search(list_,3))