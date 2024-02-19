class Magic:
    def replace(self, s, char1, char2):
        return s.replace(char1, char2)

    def str_length(self, s):
        return len(s)

    def trim(self, s):
        return s.rstrip().lstrip()

    def list_slice(self, lis, tup):
        return lis[tup[0] - 1:tup[1]]


magic = Magic()
print(magic.replace("AzERty-QwErty", 'E', 'e'))
print(magic.str_length("hello world"))
print(magic.trim("    python is awesome    "))
print(magic.list_slice([1, 2, 3, 4, 5], (2,4)))