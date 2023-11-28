def areAnagram(str1, str2):
    if len(str1) != len(str2):
        return 0
    return 1 if ''.join(sorted(str1)) == ''.join(sorted(str2)) else 0
