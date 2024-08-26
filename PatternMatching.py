# Given two strings pattern and str which may be of different size, You have to return 1
# if the wildcard pattern i.e. pattern, matches with str else return 0. All characters of 
# the string str and pattern always belong to the Alphanumeric characters.

# The wildcard pattern can include the characters ? and *
# ‘?’ – matches any single character.
# ‘*’ – Matches any sequence of characters (including the empty sequence).

# Note: The matching should cover the entire str (not partial str).

# Approach Used : Dynamic Approach similar to lcs 

class Solution:
    def wildCard(self,pattern, string):
        def isMatch(p,s):
            m=len(s)
            n=len(p)
            dp=[[False] *(n+1) for _ in range(m+1)]
            dp[0][0]=True 
            
            for i in range(1,n+1):
                if p[i-1]=='*':
                    dp[0][i]=dp[0][i-1]
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if p[j-1]=='*':
                        dp[i][j]=dp[i-1][j] or dp[i][j-1]
                    elif p[j-1]=='?' or s[i-1]==p[j-1]:
                        dp[i][j]=dp[i-1][j-1]
            return dp[m][n]
        return isMatch(pattern,string)
