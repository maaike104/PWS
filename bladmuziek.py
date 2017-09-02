import yaml


class Bladmuziek(object):
    def __init__(self, bestandsnaam):
        self.bestandsnaam = bestandsnaam
        self.muziek_info = dict()
        self.open()

    def open(self):
        with open(self.bestandsnaam) as bestand:
            tekst = bestand.read()
            self.muziek_info = yaml.load(tekst)

    def bpm(self):
        return self.muziek_info['algemeen']['bpm']

    def tonen(self):
        return self.muziek_info['algemeen']['tonen']

    def naam(self):
        return self.muziek_info['algemeen']['naam']

    def maten(self):
        return self.muziek_info['maten']
