class Solution:
    def maxPathSum(self, arr1, arr2):
        i, j = 0, 0
        m, n = len(arr1), len(arr2)
        sum1, sum2 = 0, 0
        result = 0
        
        while i < m and j < n:
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1
            elif arr1[i] > arr2[j]:
                sum2 += arr2[j]
                j += 1
            else:
                # If arr1[i] == arr2[j], we have found a common element.
                # Take the maximum of the two sums and add the common element.
                result += max(sum1, sum2) + arr1[i]
                # Reset the sums for the next segment.
                sum1 = 0
                sum2 = 0
                # Move both pointers past the common element.
                i += 1
                j += 1
        
        # Add the remaining elements in both arrays.
        while i < m:
            sum1 += arr1[i]
            i += 1
        
        while j < n:
            sum2 += arr2[j]
            j += 1
        
        # Add the maximum of the remaining sums to the result.
        result += max(sum1, sum2)
        
        return result
