class Solution(object):
    def replaceWords(self, dict, sen):
        lis = sen.split()
        A = []
        for i in range(len(lis)):
            for elem in dict:
                if elem in lis[i][:len(elem)]:
                    A.append(elem)
            if bool(A):
                lis[i] = min(A)
            del A[:]
        return ' '.join(lis)


s = Solution()
print(s.replaceWords(["a","b","c"],  "aadsfasf absbs bbab cadsfafs"))
print(s.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))