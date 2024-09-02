class Solution:
    def knapSack(self, W, wt, val):
        
        n = len(wt)
        # Initialize the DP table with zeros
        dp = [[0 for x in range(W+1)] for i in range(n+1)]
        
        # Build the DP table
        for i in range(1, n+1):
            for w in range(1, W+1):
                if wt[i-1] <= w:
                    dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
                else:
                    dp[i][w] = dp[i-1][w]
        
        # The last cell contains the maximum 
        value for the given capacity W
        return dp[n][W]
