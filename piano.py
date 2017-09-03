from os import path, getcwd
from multiprocessing import Process

from playsound import playsound


class Piano(object):
    def __init__(self, tonenmap):
        self.tonenmap = tonenmap

    def afspelen_op_achtergrond(self, toon):
        p = Process(target=self.afspelen, args=(toon,))
        p.start()

    def afspelen(self, toon):
        playsound(path.join(getcwd(), self.tonenmap, '{0}.wav'.format(toon)))
