Given two positive integer arrays arr and brr, find the number of pairs such that xy > yx (raised to power of) 
where x is an element from arr and y is an element from brr.

import bisect

class Solution:
    
    # Function to count the number of pairs (x, y) where x^y > y^x
    def countPairs(self, arr, brr):
        # Function to return count of pairs with x as one element of the pair
        # It mainly looks for all values in Y where x^Y[i] > Y[i]^x
        def count(x, Y, n, NoOfY):
            if x == 0:
                return 0
            if x == 1:
                return NoOfY[0]
            idx = bisect.bisect_right(Y, x)
            ans = n - idx
            ans += NoOfY[0] + NoOfY[1]
            if x == 2:
                ans -= NoOfY[3] + NoOfY[4]
            if x == 3:
                ans += NoOfY[2]
            return ans

        # To store counts of 0, 1, 2, 3, and 4 in array Y
        NoOfY = [0] * 5
        for value in brr:
            if value < 5:
                NoOfY[value] += 1

        # Sort brr so that we can do binary search in it
        brr.sort()
        total_pairs = 0  # Initialize result

        # Take every element of arr and count pairs with it
        for x in arr:
            total_pairs += count(x, brr, len(brr), NoOfY)

        return total_pairs
