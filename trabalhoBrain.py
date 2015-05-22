from random import randint
'''
TODO:
	-adcionar gato
	-ler mapa do arquivo

DONE:
	-tratar mapa na memória
	-movimentação do rato
	-achar rotas para o rato pelo final
'''
def novaPosAeatoriaGato(labirinto, tabelaCustos):
	x = randint(0, len(labirinto[0]))
	y = randint(0, len(labirinto))

	if labirinto[y][x] == '0':
		return aleatorioGato(labirinto, tabelaCustos)

	return x,y

moverCima = lambda x,y: (x,y-1)
moverBaixo = lambda x,y: (x, y+1)
moverDireita = lambda x,y: (x+1, y)
moverEsquerda = lambda x,y: (x-1, y)
movimentos = [moverCima,moverBaixo,moverDireita,moverEsquerda]

def acharChar(labirinto, c):
	c = c.upper()

	for y in range(0, len(labirinto)):
		for x in range(0, len(labirinto[y])):
			if labirinto[y][x] == c:
				return x,y

def acharInicio(labirinto): return acharChar(labirinto, 'S')
def acharFim(labirinto): return acharChar(labirinto, 'F')

def mover(posAtual, direcaoMovimento):
	x,y = posAtual
	return direcaoMovimento(x,y)

def possiveisMovimentos(posAtual, labirinto):
	possiveis = []

	for mov in [moverCima, moverEsquerda]:
		x, y = mover(posAtual, mov)

		if labirinto[y][x] != '0':
			possiveis.append( (x,y) )

	return possiveis



def fazRota(posRato, labirinto, gato):
	#DONE: acha as rotas de trás para frente
	rotas = []
	def loop(pos, rota):
		#TODO: adicionar excessão do gato

		r = rota[:] #copia da lista, Python trata as listas por referência
		r.append(pos)
		if pos == posRato:
			rotas.append(r)
		else:
			for p in possiveisMovimentos(pos, labirinto):
				loop(p, r)
		
		
		
	loop(acharFim(labirinto), [])
	return rotas

def addAround(labirinto):
	zeroRoll = (len(labirinto[0])+2)*'0'
	newLab = []

	for e in labirinto:
		newLab.append('0'+e+'0')

	newLab.insert(0, zeroRoll)
	newLab.append(zeroRoll)
	
	return newLab
	
	


labirinto = ['S1100',
		 	 '01100',
		 	 '01F00']
tabelaCustos = ['12500',
				'02100',
				'01400']

labirinto = addAround(labirinto)
tabelaCustos = addAround(tabelaCustos)

rato = acharInicio(labirinto)
ratoVisitada = [rato] #adiciona a posicao (0,0 como ja visitada)
#gato = novaPosAeatoriaGato(labirinto, tabelaCustos)

rotas = fazRota(rato, labirinto, (1000,1000))
for e in labirinto: print(e)
for e in rotas: print(e)
