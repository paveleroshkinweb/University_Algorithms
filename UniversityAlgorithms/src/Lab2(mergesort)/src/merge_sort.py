from helper import get_rand;
from insertion_sort import insertion_sort;
import time;

def merge_sort(array, is_hybrid = False, k = 4):
    if is_hybrid and len(array) <= k:
        insertion_sort(array)
        return array 
    elif len(array) <= 1:
        return array
    mid = int(len(array) / 2)
    return merge_arrays(merge_sort(array[:mid]), merge_sort(array[mid:]))

def merge_arrays(array1, array2):
    result = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] > array2[j]:
            result.append(array2[j])
            j+=1
        else:
            result.append(array1[i])
            i+=1
    while i < len(array1):
        result.append(array1[i])
        i+=1
    while j < len(array2):
        result.append(array2[j])
        j+=1
    return result

if __name__ == '__main__':
    length = 2
    average = 0
    for i in range(0, length):
        array = get_rand(10**3, 10**3)
        previos_time = time.time() * 1000
        merge_sort(array, True, 11)
        current_time = time.time() * 1000
        average += current_time - previos_time
    average /= length
    print(average)
