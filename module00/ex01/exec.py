import sys
len = len(sys.argv)
#for n in sys.argv[1:]: #los corchetes eliminan el primer elemento de la lista
while len > 1:
	txt = str(sys.argv[len - 1])[::-1] #los corchetes invierten el orden del string
	txt_swaped = txt.swapcase()
	if (len - 1) != 1:
		print(txt_swaped, end = ' ') 
	else:
		print(txt_swaped) 
	len -= 1
