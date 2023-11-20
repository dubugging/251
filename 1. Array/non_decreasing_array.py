def non_decreasing_array(numbers):
    changed = False

    for i in range(len(numbers)-1):
        if numbers[i+1] < numbers[i]:
            if changed:
                return False
            elif i > 0 and numbers[i-1] > numbers[i+1]:
                numbers[i+1] = numbers[i]
            else:
                numbers[i] = numbers[i+1]
            changed = True

    return True


print(non_decreasing_array(numbers=[1,2,3]))