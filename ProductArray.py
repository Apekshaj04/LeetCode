#PRODUCT OF ARRAY EXCEPT SELF 
https://www.geeksforgeeks.org/problems/product-array-puzzle4525/1

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n  # Initialize the result array with 1
        
        # Compute the prefix products
        prefix_prod = 1
        for i in range(n):
            result[i] = prefix_prod
            prefix_prod *= nums[i]
        
        # Compute the suffix products and multiply with the prefix products
        suffix_prod = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix_prod
            suffix_prod *= nums[i]
        
        return result
