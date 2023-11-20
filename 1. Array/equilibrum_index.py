def brute(numbers):
    n = len(numbers)

    for i in range(n):
        ls = 0
        rs = 0

        for j in range(i):
            ls += numbers[j]

        for k in range(i+1, n):
            rs += numbers[k]

        if ls == rs:
            return i

    return -1


def optimal(numbers):
    total = sum(numbers)
    pre_sum = 0

    for i in range(len(numbers)):
        pre_sum += numbers[i]
        if total == 2*pre_sum - numbers[i]:
            return i

    return -1


print(optimal(numbers=[1,7,3,6,5,6]))
print(optimal(numbers=[0,0,0,0,0,0]))


print(brute(numbers=[1,7,3,6,5,6]))
print(brute(numbers=[0,0,0,0,0,0]))