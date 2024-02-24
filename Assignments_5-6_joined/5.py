class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        if not grumpy:
            return sum(customers)
        else:
            total_without_tech = 0
            for i in range(len(customers) - minutes):
                if grumpy[i] == 0:
                    total_without_tech += customers[i]
            return total_without_tech + sum(customers[-minutes:])


customers = [1, 0, 1, 2, 1, 1, 3, 52]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
minutes = 3
print(Solution().maxSatisfied(customers, grumpy, minutes))