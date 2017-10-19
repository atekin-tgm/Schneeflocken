"""
@author: TEKIN Abdurrahim Burak
@date: 2017-09-29
-- Snowfall! --
"""

from threading import Thread
from random import randint
from time import sleep
import sys

# Globale Variable flockey dient als Counter für die print-position der Flocken
flockey = 0

class Schneeflocke(Thread):
    def __init__(self):
        super().__init__()

    # Methode flockenSpawn lässt die Schneeflocken erscheinen.
    # Die Idee ein randint zu verwenden, um die Flocken spawnen
    # zu lassen habe ich von einem Kollegen.
    def flockenSpawn(self):
        spawn = randint(0, 10)

        # Lässt Schneeflocken oder Leerzeichen erscheinen
        if (spawn == 1):
            print("*", end="")
        else:
            print(" ", end="")

    def run(self):
        # Mit global kann ich die globale Variable auch in meiner run-Methode verwenden
        global flockey

        # Hier wird das Grid geprinted
        print("\n====================", end="")

        # Der Counter bestimmt ab welcher Zeile die Schneeflocken erscheinen
        # (==> Scheinbarer Schneefall)
        print(flockey * "\n", end="")
        for i in range(10-flockey):
            print("")
            for j in range(20):

                # Ruft die flockenSpawn() Methode auf um potenzielle Flocken erscheinen zu lassen
                self.flockenSpawn()
        print("\n====================")
        # Der Counter für die Y-Position wird erhöht
        flockey += 1

        #print(str(flockey) + ". Line")


if __name__ == "__main__":

    # While True für automatischen Start
    while True:

        # if-Unterscheidung für das Beenden des Programms wenn alle Flocken den Boden erreicht haben
        if flockey != 10:
            t = Schneeflocke()
            t.start()
            sleep(1)
            t.join()
        else:
            print("Alle Flocken haben den Boden erreicht!")
            sys.exit(0)