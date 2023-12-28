def generateString(n):
    if n == 0:
        return ['']
    if n == 1:
        return ['0', '1']
    result = []
    for s in generateString(n-1):
        result.append(s + '0')
        if s[-1] != '1':
            result.append(s + '1')
    return result


print(generateString(n=4))
