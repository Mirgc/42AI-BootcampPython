import sys

if len(sys.argv) < 2:
	sys.exit()
elif not sys.argv[1].isdigit():
	print("AssertionError: argument is not an integer")
elif len(sys.argv) > 2:
	print("AssertionError: more than one argument are provided")
else:
	n = int(sys.argv[1])
	if n == 0:
		print("I'm Zero")
	elif (n % 2) == 0:
		print("I'm Even")
	else:
		print ("I'm Odd")
