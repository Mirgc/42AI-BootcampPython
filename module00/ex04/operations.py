import sys

def operations(A, B):
	print("Sum:\t\t", A+B)
	print("Difference:\t", A-B)
	print("Product:\t", A*B)
	if (B > 0):
		print("Quotient:\t", A/B)
		print("Reminder:\t", A%B)
	else:
		print("Quotient:\tERROR (division by zero)")
		print("Reminder:\tERROR (modulo by zero)")


if __name__ == "__main__":
	if (len(sys.argv) == 3):
		try:
			A = int(sys.argv[1])
			B = int(sys.argv[2])
			operations(A, B)
		except ValueError:
			print("AssertionError: only integers")
	elif (len(sys.argv) > 3):
		print("AssertionError: too many arguments")
	else:
		print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
