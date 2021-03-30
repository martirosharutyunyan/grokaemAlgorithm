import numpy as np
from time import perf_counter
from math import floor
from random import randint
# numpy version
# my_list = np.array([32,4,6,2,8,3,5,30,45,1,7])
my_list = 20 * np.random.random(2000)
i = 0

def quick_sort(array):
    global i
    if len(array) < 2:
        return array
    i += 1
    high = len(array) - 1
    mid = floor(high/2)
    random_number = randint(0,high)  
    pivot = array[0]
    less = array[array < pivot]
    greater = array[array > pivot]
    print('pivot',pivot,'less',less,'greater',greater)
    return np.array([*quick_sort(less),pivot,*quick_sort(greater)])

start = perf_counter()
print(quick_sort(my_list))
print(perf_counter() - start)


print(i)
# my_list = [32,4,6,2,8,3] 
# def quick_sort(array):
#     if len(array) < 2:
#         return array
#     pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array if i > pivot]
#     print('pivot',pivot,'less',less,'greater',greater)
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort(my_list))