import sys
import string

def text_analyzer(argv=None):
	'''This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.'''
	if argv is None:
		print("What is the text to analyze?")
		argv = input(">> ")
	res = isinstance(argv, str)
	if res is False:
		print("AssertionError: argument is not a string")
		return
	upper = sum(c.isupper() for c in argv)
	lower = sum(c.islower() for c in argv)
	punc = sum((c in string.punctuation) for c in argv)
	space = sum(c.isspace() for c in argv)

	print("The text contains {} characters:".format(len(argv)))
	print("- {} upper letters".format(upper))
	print("- {} lower letters".format(lower))
	print("- {} punctuation marks".format(punc))
	print("- {} spaces".format(space))

if __name__ == "__main__":
	if (len(sys.argv) == 2):
		text_analyzer(sys.argv[1])
	elif (len(sys.argv) == 1):
		text_analyzer()
	else:
		print("ERROR: More than 1 string!")
