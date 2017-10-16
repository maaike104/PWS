from Tkinter import Tk
from tkFileDialog import askopenfilename


class Bestand:
    def __init__(self):
        self.bestandsnaam = None

    def selecteer_bestand(self):
        Tk().withdraw()
        self.bestandsnaam = askopenfilename(filetypes=[('YAML', ('yaml', 'yml'))],
                                            title='Selecteer een muziekbestand')
