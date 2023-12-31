def findPossibleWords(s):
    mapp = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    ans = []

    def helper(s, temp, i):
        if i == len(s):
            ans.append(temp)
            return
        for j in range(len(mapp[s[i]])):
            helper(s, temp=temp+mapp[s[i]][j], i=i+1)

    helper(s, temp='', i=0)
    return ans


print(findPossibleWords(s='3'))
