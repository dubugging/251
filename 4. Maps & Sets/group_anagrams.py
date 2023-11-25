def getGroupedAnagrams(inputStr):
    mapp = {}
    for string in inputStr:
        sorted_word = ''.join(sorted(string, key=str.lower))
        if sorted_word not in mapp:
            mapp[sorted_word] = [string]
        else:
            mapp[sorted_word].append(string)
    
    for key in mapp:
        print(*mapp[key])


getGroupedAnagrams(inputStr=['abab', 'baba', 'aabb', 'abbc'])
