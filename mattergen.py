mat = input("De qual matéria o conteúdo o que você quer adicionar? ")
def writecont():
	global mat 
	fi = mat + ".txt" 
	print(fi)
	file = open(fi, 'w')
	cont = input("Digite o conteúdo que você deseja adicionar: ")
	file.write(cont)
	file.close()
	print("Conteúdo gravado!")
writecont()