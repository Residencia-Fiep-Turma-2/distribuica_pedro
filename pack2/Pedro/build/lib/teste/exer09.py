#!/usr/bin/python3
def showNumbers():
	limit = int(input("Digite um número: ")) 
	cont = 1
	while(cont <= limit):
		if(cont % 2):
			print(str(cont)+ " - IMPAR")
		else:
			print(str(cont)+ " - PAR")
		cont = cont+1


