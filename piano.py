# Hier zorg ik ervoor dat de computer geluid gaat maken als je op run klikt.
from os import path, getcwd
from multiprocessing import Process

from playsound import playsound


class Piano(object):
    def __init__(self, tonenmap):
        self.tonenmap = tonenmap

    """
    Hier start ik een proces zodat de computer twee tonen tegelijk kan afspelen.
    """
    def afspelen_op_achtergrond(self, toon):
        p = Process(target=self.afspelen, args=(toon,))
        p.start()
    
    """
    Hier leest de computer de audiobestanden en speelt ze af.
    """
    def afspelen(self, toon):
        playsound(path.join(getcwd(), self.tonenmap, '{0}.wav'.format(toon)))
