def better(numbers, k):
    n = len(numbers)
    k %= n
    slice = numbers[n-k:]

    for i in range(n-k-1, -1, -1):
        numbers[i+k] = numbers[i]

    for i in range(len(slice)):
        numbers[i] = slice[i]

    return numbers


def my_reverse(numbers, start, end):
    while start < end:
        numbers[start], numbers[end] = numbers[end], numbers[start]
        start += 1
        end -= 1
    return numbers


def optimal(numbers, k):
    n = len(numbers)
    k %= n
    numbers = my_reverse(numbers=numbers, start=0, end=n-k-1)
    numbers = my_reverse(numbers=numbers, start=n-k, end=n-1)
    return numbers[::-1]


print(optimal(numbers=[1, 2, 3, 4, 5, 6, 7], k=3))
