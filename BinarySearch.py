"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    finalArray = input_array
    while len(input_array) > 1:
        sizeOfList = len(input_array)
        if (sizeOfList %2) != 0:
            middleElement = input_array[int(sizeOfList / 2)]
        else:
            middleElement = input_array[int((sizeOfList / 2)-1)]

        if value == middleElement:
            return finalArray.index(middleElement)
        elif value > middleElement:
            input_array = input_array[:(input_array.index(middleElement))]
        elif value < middleElement:
            input_array = input_array[(input_array.index(middleElement)+1):]

    

    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 11
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))

# v2

def binary_search(input_array, value):
    low = 1
    high = len(input_array)
   

    while low <= high:
        mid = (low + high)/2
        if input_array[mid] == value:
            return mid
            break
        elif input_array[mid] > value:
            low = mid +1
        else :
            high = mid -1
    
    return -1


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))
