#from model.Labirinto import Labirinto
#from model.Labirinto import labirintoFileFactory
from model.Labirinto import *


#labirinto, tabelaCustos = carregarArquivo("labirinto")
#lab = Labirinto(labirinto, tabelaCustos)
lab = labirintoFileFactory("labirinto")
rotas = lab.fazRotas(lab.rato)


#gato = posAleatoriaGato(labirinto)
#rato = acharInicio(labirinto)

#rotas = fazRota(rato, labirinto, gato)

#visualizar o gato e o rato
for y in range(len(lab.labirinto)):
	a = ""
	for x in range(len(lab.labirinto[y])):
		if (x, y) == lab.gato:
			a+="G"
		elif (x,y) == lab.rato:
			a+="R"
		else:
			a+=lab.labirinto[y][x]
	print(a)

#menor rota com base na posicao do gato
#print(acharMenorRota(rotas, tabelaCustos, gato))
print(lab.fazRotas(lab.rato))