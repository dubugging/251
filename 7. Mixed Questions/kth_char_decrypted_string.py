def kThCharaterOfDecryptedString(s, k):
    n = len(s)
    substring = ''
    decryptedString = ''
    i = 0

    while (i < n):
        j = i
        substring = ''
        freqOfSubstring = 0

        while (j < n and s[j].islower()):
            substring += s[j]
            j += 1

        while (j < n and s[j].isdigit()):
            freqOfSubstring = freqOfSubstring * 10 + (ord(s[j]) - ord('0'))
            j += 1

        i = j

        while (freqOfSubstring > 0):
            decryptedString += substring
            freqOfSubstring -= 1

    return decryptedString[k-1]
