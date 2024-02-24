class Solution(object):
    def waysToBuyPensPencils(self, total, cost1, cost2):
        if total == 0 or total < cost1 and total < cost2:
            return 1
        else:
            count = 0
            for i in range(total // cost2):
                if count < total // cost2:
                    count += (total // cost2) + 1
                else:
                    if total - (cost1 * i) == 0:
                        break
                    else:
                        count += (total - cost1 * i) // cost2 + 1 + i
        return count


total = 5
cost1 = 10
cost2 = 10
print(Solution().waysToBuyPensPencils(total,cost1,cost2))