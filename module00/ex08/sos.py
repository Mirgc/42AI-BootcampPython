import sys
import string

morse_code = {65: '.-',66: '-...',67: '-.-.',68: '-..',69: '.',70: '..-.',71: '--.',72: '....',73: '..',
74: '.---',75: '-.-',76: '.-..',77: '--',78: '-.',79: '---',80: '.--.',81: '--.-',82: '.-.',83: '...',
84: '-',85: '..-',86: '...-',87: '.--',88: '-..-',89: '-.--',90: '--..',48: '-----',49: '.----',
50: '..---',51: '...--',52: '....-',53: '.....',54: '-....',55: '--...',56: '---..',57: '----.'}

lst = []

def ft_morse(argv):
	txt = " ".join(argv).upper()
	lst = []
	for s in txt:
		if s in string.punctuation:
			print("ERROR")
			exit()
		elif s == ' ':
			lst.append('/')
		else:
			lst.append(s.translate(morse_code))
	s_morse = " ".join(lst)
	print(s_morse)

if __name__ == "__main__":
	if len(sys.argv) > 1:
		ft_morse(sys.argv[1:])
