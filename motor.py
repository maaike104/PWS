class Motor(object):
    def __init__(self, toon, bpm=None):
        self.toon = Toon(toon)
        self.bpm = bpm
        
    def afspelen(self):
        print(self.toon)
        
    def __str__(self):
        return 'Motor {0} {1}'.format(self.toon, self.bpm)
        
    def __repr__(self):
        return self.__str__()


class Toon(object):
    def __init__(self, toon):
        self.toon = toon
        
    def __str__(self):
        return self.toon
