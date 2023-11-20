def handle_odd(s, n):
	if n == 1: return s
	left = s[:n//2]
	mid = s[n//2]
	right = s[n//2+1:]

	if left[::-1] > right: return left+mid+left[::-1]
	else:
		if mid < '9': return left+str(int(mid)+1)+left[::-1]
		else:
			pre = str(int(left+mid) + 1)
			return pre+pre[:n//2][::-1]


def handle_even(s, n):
	left = s[:n//2]
	right = s[n//2:]

	if left[::-1] < right:
		left = str(int(left)+1)
		return left+left[::-1]
	return left+left[::-1]


def nextLargestPalindrome(s):
	if s == s[::-1]:
		s = str(int(s)+1)

	n = len(s)

	if n == 1:
		return s

	if n % 2 == 1: return handle_odd(s, n)
	return handle_even(s, n)


print(nextLargestPalindrome(s='8'))
