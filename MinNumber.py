class Solution:
    def minOperations(self, str1, str2):
        m = len(str1)
        n = len(str2)
        
        # Create a DP table to store lengths of LCS
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill dp array (similar to LCS problem)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Length of LCS is dp[m][n]
        lcs = dp[m][n]
        
        # Minimum operations = (m - lcs) deletions + (n - lcs) insertions
        deletions = m - lcs
        insertions = n - lcs
        
        return deletions + insertions
