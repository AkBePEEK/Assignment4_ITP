def getHint(secret, guess, bulls=0):
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
    cows = len(secret) - bulls
    return str(bulls)+'A'+str(cows)+'B'


print(getHint('1807', '7810'))