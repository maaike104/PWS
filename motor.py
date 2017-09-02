TONES = ('C', 'D', 'E', 'F', 'G', 'A', 'B', 'c', 'd', 'e', 'f')

class Motor(object):
    def __init__(self, tone):
        self.tone = tone
        
    def __str__(self):
        return 'Motor {0}'.format(self.tone)
        
    def __repr__(self):
        return self.__str__()


class Tone(object):
    def __init__(self, tone):
        self.tone = tone
        
    def __str__(self):
        return self.tone

motors = list()
for tone in TONES:
    motors.append(Motor(tone))

print(motors)
