from controleMapa import *
from loadFile import carregarArquivo


labirinto, tabelaCustos = carregarArquivo("labirinto")

gato = posAleatoriaGato(labirinto)
rato = acharInicio(labirinto)

rotas = fazRota(rato, labirinto, gato)
'''
for e in labirinto:
    print(e)
for e in rotas:
    print(e)
'''

for y in range(len(labirinto)):
	a = ""
	for x in range(len(labirinto[y])):
		if (x, y) == gato:
			a+="G"
		elif (x,y) == rato:
			a+="R"
		else:
			a+=labirinto[y][x]
	print(a)

print(acharMenorRota(rotas, tabelaCustos, gato))