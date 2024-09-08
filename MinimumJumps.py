class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n == 1:
            return 0  # No jump needed if we are already at the end
        if arr[0] == 0:
            return -1  # If the first element is 0, we can't move anywhere
        
        # Initializing the number of jumps, the current end, and the farthest reachable index
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n):
            farthest = max(farthest, i + arr[i])  # Update the farthest we can reach
            if i == current_end:
                if i != n - 1:
                    jumps += 1
                    current_end = farthest
                    if current_end >= n - 1:
                        return jumps
                else:
                    return jumps
            if i == current_end and farthest == i:
                return -1  # We are stuck, cannot move further
        
        return -1
