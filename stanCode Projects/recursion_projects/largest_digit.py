"""
File: largest_digit.py
Name: Ruby
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, offered integer
	:return: int, highest digit searched by helper function
	"""
	highest = 0
	return helper(n, highest)

def helper(n, highest):
	n = abs(n)
	if n == 0:
		return highest
	else:
		last_digit = n % 10
		if last_digit >= highest:
			highest = last_digit
		return helper(n//10, highest)


if __name__ == '__main__':
	main()
