def generate(n, start='0', end='1'):
    if not n:
        return ''
        
    ans = ''
    for i in range(n):
        if i % 2 == 0:
            ans += start
        else:
            ans += end
    return ans


def diff(original, generated):
    count = 0
    for i in range(len(original)):
        if original[i] != generated[i]:
            count += 1
    return count


def make_beautiful(str):
    n = len(str)
    str1 = generate(n)
    str2 = generate(n, '1', '0')
    return min(diff(str, str1), diff(str, str2))


print(make_beautiful(str='11111'))