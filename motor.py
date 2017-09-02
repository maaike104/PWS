class Motor(object):
    def __init__(self, toon):
        self.toon = toon

    def afspelen(self):
        # TODO Zodra we met echte motoren gaan werken moeten we hier zorgen dat onze machine
        # TODO geluid gaat maken.
        print(self.toon)
