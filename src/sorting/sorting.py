# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []

    # Start by comparing the first elements of each arr
    arrA_index = 0
    arrB_index = 0

    # Repeat this loop if there are elements left to go through in both arrays
        # So when the index has past the end of the len of one of the arrays, stop
    # When there is not, add the remainder of both lists to the end of merged list
        # In one case the array will be empty, so nothing will be added
        # In the other case the remaining elements will already have been sorted and have nothing to be compared to
    while arrA_index < len(arrA) and arrB_index < len(arrB):

        # If the arrayA element is less than the arrayB element
        if arrA[arrA_index] < arrB[arrB_index]:
            # Add the arrayA element to merged array first
            merged_arr.append(arrA[arrA_index])
            # Then move the index pointer 1 over in the arrayA
            arrA_index += 1

        # Otherwise (if element in arrB is less than or equal to), add arrB element to the merged array
        else:
            # Add the arrayB element to merged array first
            merged_arr.append(arrB[arrB_index])
            # Then move the index pointer 1 over in the arrayB
            arrB_index += 1

    # When the index has been moved outside of either array (meaning one has been completely sorted already)
    # Add the remaining elements to the merged array

    # Add the remainder of arrA
    merged_arr += arrA[arrA_index:]

    # Add the remainder of arrB
    merged_arr += arrB[arrB_index:]

    # Return sorted array from array A and B
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):

    # Make sure the array being passed in is greater than 1 otherwise it doesn't need to be sorted
    if len(arr) > 1:
        # Divide the input array in half
        mid = len(arr) // 2

        # Save the left and right halves to further divide or merge together later
        left = arr[:mid]
        # The half way point is included in the right side
        right = arr[mid:]

        # Check the left and right sides to see if they can be divided in half again
        # If it can, call merge_sort again
            # (this will open up a new call on the left array only that will divide it in half
            # and check to see if it can be divided again, if it can it will open another call and so on...)
        if len(left) > 1:
            left = merge_sort(left)
        # Check right side to see if it can be divided in half
        if len(right) > 1:
            right = merge_sort(right)
        # After the left and right sides can no longer be divided in half, 
        # start merging them together, working backwards
        # As it moves back up the recursive calls, it will add the smaller pieces until its all one array
        arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# # In other words, your implementation should not allocate any additional lists 
# # or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

