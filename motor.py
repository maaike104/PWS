class Motor(object):
    def __init__(self, toon):
        self.toon = toon

    def afspelen(self):
        # Omdat we nu nog geen echte motors gebruiken wegens geldgebrek is dit nu nutteloos, in plaats daarvan hebben we nu het bestandje
        # piano.py waar in plaats van onze knikkerbaan de computer het geluid maakt.
        print(self.toon)
