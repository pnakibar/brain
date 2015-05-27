from model.labirinto import *
from control.gameControl import *
from view.gameWindow import *

a = GameControl('/home/pedronakibar/git/TPA/brain/lab')
sc = Screen(a)
sc.run()
