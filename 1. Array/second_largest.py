def find_second_largest(numbers):
    largest = max(numbers)
    second_largest = min(numbers)

    if largest == second_largest:
        return -1

    for number in numbers:
        if largest > number > second_largest:
            second_largest = number

    return second_largest


print(find_second_largest(numbers=[6, 6, 6, 5]))
