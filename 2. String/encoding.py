def encode(message):
    result = ''
    count = 1
    for i in range(len(message)-1):
        if message[i] != message[i+1]:
            result += message[i] + str(count)
            count = 1
        else:
            count += 1
    return result + message[-1] + str(count)


print(encode(message='aaaa'))