#!/usr/bin/python3
def verifica_velocidade():
	velocidade = int(input("Digite a velocidade em km/h: "))
	if(velocidade >= 70):
		velocidade = velocidade-70
		pontos = int(velocidade/5)
		print("Pontos: "+ str(pontos))
		if(pontos > 12):
			print("Licença suspensa")
	else:
		print("ok")


