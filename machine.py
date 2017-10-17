# importeer de module time zodat we 'm kunnen gebruiken in de code
import time
# importeer van de andere bestanden de classes zodat we deze kunnen gebruiken
from motor import Motor
from bladmuziek import Bladmuziek
from piano import Piano
from bestand import Bestand

# constant (dus hoofdletters)
MINUUT = 60


# machine is de 'baas' die tegen de motoren praat
class Machine(object):
    def __init__(self, bestandsnaam):
        """
        Stel het Machine object in met de motoren en de informatie die uit de Bladmuziek
        class gehaald wordt.
        """
        self.motors = dict()
        self.bladmuziek = Bladmuziek(bestandsnaam)
        self.piano = Piano('tonen')
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
        for naam, maat in sorted(self.maten.iteritems()):
            print(naam)
            for tel, tonen in maat.iteritems():
                # MINUUT / bpm betekent dat je het interval tussen twee tellen krijgt. Je wacht met
                # sleep dus totdat je weer een tel hebt.
                time.sleep(MINUUT / float(self.bpm))
                # Speel de tonen af die deze tel langskomen met de juiste motor.
                if tonen:
                    for toon in tonen:
                        self.motors[toon].afspelen()
                        self.piano.afspelen_op_achtergrond(toon)
