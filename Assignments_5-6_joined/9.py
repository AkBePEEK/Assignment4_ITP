class Solution:
    def taskSchedulerII(self, tasks: list[int], space: int) -> int:
        mp = {}
        ans = 0
        for elem in tasks:
            ans += 1
            ans = max(ans, mp.get(elem, 0))
            mp[elem] = ans + space + 1
        return ans


s = Solution()
print(s.taskSchedulerII([1,2,1,2,3,1], 3))