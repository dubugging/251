def rev(string, start, end):
    if start >= end:
        return string
    string[start], string[end] = string[end], string[start]
    return rev(string, start+1, end-1)


print(rev(string=list('abcd'), start=0, end=3))
