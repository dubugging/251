def kthChildNthGeneration(n, k):
    if (n == 1 or k == 1):
        return "M"

    par = (k + 1) // 2
    parGender = kthChildNthGeneration(n - 1, par)

    if (k == 2*par-1):
        return parGender
    else:
        if (parGender == "M"):
            return "F"
        return "M"


print(kthChildNthGeneration(n=3, k=2))
