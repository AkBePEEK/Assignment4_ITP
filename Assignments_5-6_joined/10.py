class Solution(object):
    def candy(self, ratings):
        if not ratings:
            return 0
        else:
            ratings = sorted(ratings)
            child = 0
            for i in range(len(ratings)):
                child += 1
                print(ratings[i], ratings[i - 1])
                if ratings[i] > ratings[i - 1]:
                    child += 1
            return child


ratings = [1,2,2]
print(Solution().candy(ratings))