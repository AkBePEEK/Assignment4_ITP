def consonants(a, vowels=['a', 'e', 'o', 'u', 'i']):
    return list(filter(lambda x: len(x) == len([elem for elem in x if elem not in vowels]), a))


print(consonants(["Hello","World","Python","GPT","Str","Rhythm","Fly","Brr","Crypt","Sky","Phy","Gym","Synth","Grn","Blk","Cycl"]))