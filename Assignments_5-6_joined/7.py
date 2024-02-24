class Solution:
    def closestCost(self, baseCosts: list[int], toppingCosts: list[int], target: int) -> int:
        ans = baseCosts[0]
        li = baseCosts
        for cost in toppingCosts:
            for c in li.copy():
                li.append(c + cost)
                li.append(c + 2 * cost)
        for a in li:
            if abs(a - target) < abs(ans - target) or abs(a - target) == abs(ans - target) and a < ans:
                ans = a
        return ans


s = Solution()
print(s.closestCost([2,3], [4,5,100], 18))