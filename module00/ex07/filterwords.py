import sys
import string

def ft_split(s, n):
	s = s.translate(s.maketrans('', '', string.punctuation)) #elimina los signos de puntuacion
	txt = s.split()
	lst = [] 
	for i in txt:
		if len(i) > int(n):
			lst.append(i)
	print(lst)

if __name__ == "__main__":
	res = isinstance(sys.argv[1], str)
	if len(sys.argv) != 3:
		print("ERROR")
	elif res is False:
		print("ERROR", sys.argv[1])
	elif not sys.argv[2].isdigit():
		print("ERROR")
	else:
		ft_split(sys.argv[1], sys.argv[2])
