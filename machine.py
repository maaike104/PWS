# importeer de module time zodat we 'm kunnen gebruiken in de code
import time
# importeer van de andere bestanden de classes zodat we deze kunnen gebruiken
from motor import Motor
from bladmuziek import Bladmuziek

# constant (dus hoofdletters)
MINUUT = 60


# machine is de 'baas' die tegen de motoren praat
class Machine(object):
    def __init__(self):
        """
        Stel het Machine object in met de motoren en de informatie die uit de Bladmuziek
        class geplukt wordt.
        """
        self.motors = dict()

        # FIXME Dit is niet zo netjes: er kan nu geen ander YAML bestand gebruikt worden!
        self.bladmuziek = Bladmuziek('pachelbel.yml')

        self.tonen = self.bladmuziek.tonen()
        self.bpm = self.bladmuziek.bpm()
        self.naam = self.bladmuziek.naam()
        self.maten = self.bladmuziek.maten()
        
        self.maak_motors()
    
    def maak_motors(self):
        """
        Maak een motor voor elke toon en stop die in een dictionary met
        naam 'toon' en waarde 'motor'.
        """
        for toon in self.tonen:
            self.motors[toon] = Motor(toon)
    
    def afspelen(self):
        """
        Speel elke maat af. Elke maat heeft een vast aantal tellen, en per tel kunnen er
        meeerdere tonen zijn die moeten worden afgespeeld.
        """
        for naam, maat in self.maten.items():
            for tel, tonen in maat.items():
                # MINUUT / bpm betekent dat je het interval tussen twee tellen krijgt. Je wacht met
                # sleep dus totdat je weer een tel hebt.
                time.sleep(MINUUT / self.bpm)
                # Speel de tonen af die deze tel langskomen met de juiste motor.
                for toon in tonen:
                    self.motors[toon].afspelen()


if __name__ == '__main__':
    machine = Machine()
    # print(machine.motors)
    machine.afspelen()
