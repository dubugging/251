def firstNonRepeatingCharacter(str):
    dic = {}
    for char in str:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1

    x = list(filter(lambda item: item[1] == 1, dic.items()))

    return x[0][0]


print(firstNonRepeatingCharacter(
    str='ylbbdirddtyuylyhfbihwamrkwixekedcqspmsvgjgnsshrfechmvqfdmubwdufybtanjqcjamcwwr'))
