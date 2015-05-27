from model.labirinto import *
from control.gameControl import *
from view.gameWindow import *

a = GameControl('brain/lab')
sc = Screen(a)
sc.run()
