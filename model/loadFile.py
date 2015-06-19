'''
funcoes para abrir o mapa de um arquivo
exemplo de arquivo:

labirinto
S1100
01100
01F00

custos
12500
02100
01400

'''
def addAround(labirinto):
    zeroRoll = (len(labirinto[0]) + 2) * '0'
    newLab = []

    for e in labirinto:
        newLab.append('0' + e + '0')

    newLab.insert(0, zeroRoll)
    newLab.append(zeroRoll)

    return newLab

def limparLista(l):
	'''
	remove elementos vazios, strings vazias e "carriage returns"
	'''
	for i in range(0, len(l)):
		l[i] = l[i].replace("\n", "")
		if (l[i] == None) or (l[i] == ""): l.pop(i)

def carregarArquivo(filename):
	file = open(filename, 'r')
	labirinto = []
	tabelaCustos = []

	lines = file.readlines()

	toLoad = None

	for e in lines:
		if "labirinto" in e:
			toLoad = labirinto

		elif "custos" in e:
			toLoad = tabelaCustos

		elif toLoad != None:
			toLoad.append(e)


	file.close()

	limparLista(labirinto)
	limparLista(tabelaCustos)
	labirinto = addAround(labirinto)
	tabelaCustos = addAround(tabelaCustos)

	return labirinto, tabelaCustos
