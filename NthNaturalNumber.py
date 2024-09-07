class Solution:
    def findNth(self, n):
        result = 0
        base = 1
        
        # Convert n to its equivalent in base-9
        while n > 0:
            result += (n % 9) * base
            n //= 9
            base *= 10
        
        return result
