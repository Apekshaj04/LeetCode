'''Given an integer array arr of integers, the task is to find the maximum absolute difference between the nearest left
smaller element and the nearest right smaller element of every element in array arr. If for any component of the arr, the nearest 
smaller element doesn't exist then consider it as 0.'''
class Solution:
    def findMaxDiff(self, arr):
        n = len(arr)
        
        # Arrays to store the nearest smaller elements
        left = [0] * n
        right = [0] * n
        
        # Stack to find nearest left smaller elements
        stack = []
        for i in range(n):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            else:
                left[i] = 0
            stack.append(arr[i])
        
        # Clear the stack to reuse it for right smaller elements
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            else:
                right[i] = 0
            stack.append(arr[i])
        
        # Calculate the maximum absolute difference
        max_diff = 0
        for i in range(n):
            max_diff = max(max_diff, abs(left[i] - right[i]))
        
        return max_diff
