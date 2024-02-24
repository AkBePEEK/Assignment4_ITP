class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        ans = 0
        maxim = 0
        for i in range(len(customers)):
            if minutes + i <= len(customers) - 1:
                for j in range(i, minutes + i):
                    if maxim < customers
        for i in range(len(customers)):
            if grumpy[i] == 0:
                ans += customers[i]