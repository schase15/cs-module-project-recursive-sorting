# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    # Base case: When the entire array has been searched and the target not found
        # When the start passes the end of the search area
        # Or the end is moved lower than the starting position
        # Return -1
    if start > end:
        return -1

    # Compare the midpoint to the target
    # Calculate the midpoint of the portion of the array we are searching
    midpoint = (start + end) // 2

    # Stop when the target == the value
    # Return midpoint index
    if target == arr[midpoint]:
        return midpoint

    # If target is is greater than midpoint, toss out the left half, repeat the search with the right half
    if target > arr[midpoint]:
        # Re-assign the starting point to 1 past the midpoint
        start = midpoint +1
        # Re-call the method
        # Pass in new starting point. End point, arr, and target are the same
        return binary_search(arr, target, start, end)

    # If it is less than, toss out the right half, repeat the search with the left half
    if target < arr[midpoint]:
        # Re-assign the ending point to one before the midpoint
        end = midpoint -1
        # Re-call the method
        # Pass in new ending point. Start point, arr, and target are the same
        return binary_search(arr, target, start, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# # or iteratively
def agnostic_binary_search(arr, target):
    # Check if the list is ascending or descending and handle it accordingly
    start = 0
    end = len(arr)-1
    # if the first value is less than the last, it is ascending
    # If the first value is equal to the last than it can be treated as ascending
    if arr[0] < arr[-1]:
        ascending = True
    else:
        ascending = False

    if ascending:
        # If it is ascending, use the method defined in part 1
        binary_search(arr, target, 0, len(arr) -1)
    
    # Otherwise, rework part 1 to work with descending 
    else:

        