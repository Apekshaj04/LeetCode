class Solution:
    def missingNumber(self, n, arr):
        # Calculate the expected sum of the first n numbers
        total_sum = n * (n + 1) // 2
        
        # Calculate the sum of the elements in the array
        array_sum = sum(arr)
        
        # The missing number will be the difference between total_sum and array_sum
        return total_sum - array_sum
