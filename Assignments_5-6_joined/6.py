class Solution(object):
    def maxSumDivThree(self, nums):
        dp = [0,0,0]
        for i in nums:
            for j in dp[:]:
                dp[(j + i) % 3] = max(dp[(j + i) % 3], j + i)
        return dp[0]


nums = [1,2,3,4]
print(Solution().maxSumDivThree(nums))