#!/bin/python
def print_array(array):
    array_str = ''
    for n in range(len(array)):
        array_str += str(array[n]) + ' '
    print array_str    

def insert_element(ar, i):
    unsorted = True
    temp = ar[i]
    
def insertionSort(ar):
    last_index = len(ar) - 1
    unsorted = True
    temp = ar[last_index]
    while unsorted:
        if last_index == 0:
            ar[last_index] = temp
            unsorted = False
        elif ar[last_index-1] > temp:
            ar[last_index] = ar[last_index -1]
        else:
            ar[last_index] = temp
            unsorted = False
        print_array(ar)
        last_index -= 1
            
    return ""

# Tail starts here