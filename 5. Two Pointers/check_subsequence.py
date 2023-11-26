# str2 is original
# str1 is sub sequence

def isSubSequence(str1, str2):
    n = len(str1)
    pointer = 0
    for i in range(len(str2)):
        if str2[i] == str1[pointer]:
            pointer += 1
    return True if pointer == n else False


print(isSubSequence(str1='ABC', str2='AHBDGC'))
