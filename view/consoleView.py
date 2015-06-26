import os
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
def printSplash():
    splash = '''
    d8888b. d8888b.  .d8b.  d888888b d8b   db 
    88  `8D 88  `8D d8' `8b   `88'   888o  88 
    88oooY' 88oobY' 88ooo88    88    88V8o 88 
    88~~~b. 88`8b   88~~~88    88    88 V8o88 
    88   8D 88 `88. 88   88   .88.   88  V888 
    Y8888P' 88   YD YP   YP Y888888P VP   V8P 
    '''

    print(bcolors.BOLD + bcolors.FAIL + splash + bcolors.ENDC )


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Screen:
        def __init__(self, gameController):
            self.gameController = gameController
            self.cat =  bcolors.BOLD + bcolors.FAIL + 'C' + bcolors.ENDC
            self.mouse = bcolors.BOLD + bcolors.OKGREEN + 'M' + bcolors.ENDC
            self.floor = ' '
            self.background = '#'
            

        def drawLabirinto(self):
            lab = self.gameController.getLabirinto()

            for y in range(len(lab)):
                buffer = ""
                for x in range(len(lab[y])):
                    tile = lab[y][x]
                    if (x, y) == self.getGatoPos():
                        buffer+=self.cat
                    elif (x, y) == self.getRatoPos():
                        buffer+=self.mouse
                    elif tile == '0':
                        buffer+=self.background
                    else:
                        buffer+=self.floor

                print(buffer)

        
        def run(self):
            printSplash()
            raw_input("Pressione enter para continuar...")
            error = False

            while (True):
                clearScreen()
                self.drawLabirinto()
                if self.gameController.acabouJogo:
                    if self.gameController.ratoVivo:
                        print(bcolors.BOLD + bcolors.OKGREEN + "Voce ganhou!" + bcolors.ENDC)
                    
                    else:
                        if error:
                            print(bcolors.BOLD + bcolors.WARNING + "Nao tem rota ate o final!" + bcolors.ENDC)

                        print(bcolors.BOLD + bcolors.FAIL + "Voce perdeu!" + bcolors.ENDC)
                        

                    raw_input("Presione enter para terminar...")
                    break
                else:
                    raw_input("Pressione enter para continuar...")
                    try:
                        self.gameController.rodaTurno()
                    except Exception:
                        error = True

        def getGatoPos(self):
            gatoX, gatoY = self.gameController.getGatoPos()
            return gatoX, gatoY

        def getRatoPos(self):
            mouseX, mouseY = self.gameController.getRatoPos()
            return mouseX, mouseY
