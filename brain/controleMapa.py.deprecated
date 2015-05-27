from random import randint


def posAleatoriaGato(labirinto):
    x = randint(0, len(labirinto[0])-1)
    y = randint(0, len(labirinto)-1)
    if labirinto[y][x] == '0':
        return posAleatoriaGato(labirinto)

    return x, y

moverCima = lambda x, y: (x, y - 1)
moverBaixo = lambda x, y: (x, y + 1)
moverDireita = lambda x, y: (x + 1, y)
moverEsquerda = lambda x, y: (x - 1, y)
movimentos = [moverCima, moverBaixo, moverDireita, moverEsquerda]


def acharChar(labirinto, c):
    c = c.upper()

    for y in range(0, len(labirinto)):
        for x in range(0, len(labirinto[y])):
            if labirinto[y][x] == c:
                return x, y


def acharInicio(labirinto):
    return acharChar(labirinto, 'S')


def acharFim(labirinto):
    return acharChar(labirinto, 'F')


def mover(posAtual, direcaoMovimento):
    x, y = posAtual
    return direcaoMovimento(x, y)


def possiveisMovimentos(posAtual, labirinto):
    possiveis = []

    for mov in [moverCima, moverEsquerda]:
        x, y = mover(posAtual, mov)

        if labirinto[y][x] != '0':
            possiveis.append((x, y))

    return possiveis



def fazRota(posRato, labirinto, gato):
    # DONE: acha as rotas de tras para frente
    rotas = []

    def loop(pos, rota):
        r = rota[:]  # copia da lista, Python trata as listas por referencia
        r.append(pos)
        if (pos == posRato):
            rotas.append(r)
        else:
            for p in possiveisMovimentos(pos, labirinto):
            	loop(p, r)

    loop(acharFim(labirinto), [])
    return rotas

def calcularCustoRota(rota, tabelaCustos, gato):
	peso = 0
	for x, y in rota:
		if (x,y) == gato:
			peso = peso + float("inf")
		else:
			peso = peso + int(tabelaCustos[y][x])

	return peso

def acharMenorRota(rotasPossiveis, tabelaCustos, gato):
	menorRota = rotasPossiveis[0]
	menorPesoRota = calcularCustoRota(menorRota, tabelaCustos, gato)

	for e in rotasPossiveis:
		pesoRota = calcularCustoRota(e, tabelaCustos, gato)

		if menorPesoRota > pesoRota:
			menorPesoRota = pesoRota
			menorRota = e

	return menorRota, menorPesoRota


