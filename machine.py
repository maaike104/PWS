import time

from motor import Motor
from bladmuziek import Bladmuziek


MINUUT = 60


class Machine(object):
    def __init__(self):
        self.motors = list()
        self.bladmuziek = Bladmuziek('pachelbel.yml')
        self.tonen = self.bladmuziek.tonen()
        self.bpm = self.bladmuziek.bpm()
        self.naam = self.bladmuziek.naam()
        self.maten = self.bladmuziek.maten()
        
        self.maak_motors()
    
    def maak_motors(self):
        for toon in self.tonen:
            self.motors.append(Motor(toon, 2*self.bpm))
    
    def __str__(self):
        return str(self.motors)
    
    def afspelen(self):
        for i in range(0, 100):
            time.sleep(MINUUT / self.bpm)
            print('BEAT {0}'.format(i))
            for m in self.motors:
                m.afspelen()


if __name__ == '__main__':
    machine = Machine()
    machine.afspelen()