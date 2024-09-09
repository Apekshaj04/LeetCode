class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        low = 0
        mid = 0
        high = len(arr) - 1

        # Traverse the array and sort it
        while mid <= high:
            if arr[mid] == 0:
                # Swap arr[low] and arr[mid] and move both pointers forward
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                # If the element is 1, just move the mid pointer forward
                mid += 1
            else:
                # If the element is 2, swap arr[mid] and arr[high], and move high pointer backward
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr
