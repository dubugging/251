def reverseStringWordWise(string):
    words = string.split(' ')
    result = ''
    
    for i in range(len(words)-1, -1, -1):
        result += words[i] + ' '

    return result


print(reverseStringWordWise(string='Welcome to Coding Ninjas'))