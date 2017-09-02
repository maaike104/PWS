import time

from motor import Motor
from bladmuziek import Bladmuziek


MINUUT = 60


class Machine(object):
    def __init__(self):
        self.motors = dict()
        self.bladmuziek = Bladmuziek('pachelbel.yml')
        self.tonen = self.bladmuziek.tonen()
        self.bpm = self.bladmuziek.bpm()
        self.naam = self.bladmuziek.naam()
        self.maten = self.bladmuziek.maten()
        
        self.maak_motors()
    
    def maak_motors(self):
        for toon in self.tonen:
            self.motors[toon] = Motor(toon, 2*self.bpm)
    
    def __str__(self):
        return str(self.motors)
    
    def afspelen(self):
        for naam, maat in self.maten.items():
            for noot, tonen in maat.items():
                time.sleep(MINUUT / self.bpm)
                for toon in tonen:
                    self.motors[toon].afspelen()

if __name__ == '__main__':
    machine = Machine()
    # print(machine.motors)
    machine.afspelen()