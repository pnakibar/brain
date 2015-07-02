#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Pedro Mathias Nakibar - @pnakibar - pedronakibar@gmail.com
Programa feito para a disciplina de TPA para o curso de Sistemas de Informação do IFES Serra
Caos não consiga rodar favor ler o README.md e seguir as instruções!
Lembre-se de instalar o pygame!
'''
from model.labirinto import *
from control.gameControl import *
import sys

if sys.argv[1] == '-pygame':
    from view.gameView import *
else:
    from view.consoleView import *
'''
    carregar jogo
    sem argumento carrega o padrao
'''

a = GameControl(sys.argv[-1])

sc = Screen(a)
sc.run()
