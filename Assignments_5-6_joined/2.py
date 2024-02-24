class Solution(object):
    def climbStairs(self,n):
        L = [0 for i in range(n+1)]
        L[0], L[1] = 1, 1
        for i in range(2, n+1):
            L[i] = L[i - 1] + L[i - 2]
        return L[n]
