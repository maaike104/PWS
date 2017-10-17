# yaml is van library pyaml (van iemand anders, zie http://pyyaml.org/wiki/PyYAMLDocumentation)
# en kan .yml bestanden lezen en schrijven. Hiermee kan dus een vertaling van tekst naar Python
# worden gemaakt.
import yaml


# Bladmuziek leest een .yml bestand en vertaalt het naar Python.
class Bladmuziek(object):
    def __init__(self, bestandsnaam):
        self.bestandsnaam = bestandsnaam
        self.muziek_info = dict()
        self.open()

    def open(self):
        """
        Lees het bestand en vertaal YAML naar Python. Dit wordt opgeslagen in muziek_info,
        een dictionary.
        TESTESTESTEST
        """
        with open(self.bestandsnaam) as bestand:
            tekst = bestand.read()
            self.muziek_info = yaml.load(tekst)

    def bpm(self):
        """
        Pluk bpm uit de dictionary muziek_info.
        """
        return self.muziek_info['algemeen']['bpm']

    def tonen(self):
        """
        Pluk de tonen uit de dictionary muziek_info.
        """
        return self.muziek_info['algemeen']['tonen']

    def naam(self):
        """
        Pluk naam uit de dictionary muziek_info.
        """
        return self.muziek_info['algemeen']['naam']

    def maten(self):
        """
        Pluk maten uit de dictionary muziek_info.
        """
        return self.muziek_info['maten']
