from model.labirinto import *
from control.gameControl import *
import sys

if sys.argv[1] == '-pygame':
    from view.gameWindow import *
else:
    from view.consoleView import *
'''
    carregar jogo
    sem argumento carrega o padrao
'''

a = GameControl(sys.argv[-1])

sc = Screen(a)
sc.run()
