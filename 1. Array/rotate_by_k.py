def rotate_by_k(numbers, k):
    k %= len(numbers)
    others = numbers[k:]

    for i in range(k):
        numbers[-1-i] = numbers[k-i-1]

    for i in range(len(others)):
        numbers[i] = others[i]

    return numbers


print(rotate_by_k(numbers=[1,2,3,4,5,6,7,8,9], k=4))