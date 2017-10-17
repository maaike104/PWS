# Tkinter is een standaard schermpje dat van Python dat je kan aanroepen zodat er een soort keuzemenu tevoorschijn komt, 
# en die importeer ik hier zodat ik deze kan aanroepen en het bestand wat ik af wil laten spelen kan kiezen.
from Tkinter import Tk
# Tkinter gaat voor mij een beschikbaar bestand zoeken en daarvoor heb ik askopenfilename nodig
from tkFileDialog import askopenfilename


class Bestand:
    def __init__(self):
        self.bestandsnaam = None

    def selecteer_bestand(self):
        Tk().withdraw()
        """
        De code kan alleen een yaml bestand lezen, dus hier zeg ik dat het bestandtype .yml of .yaml moet zijn.
        """
        self.bestandsnaam = askopenfilename(filetypes=[('YAML', ('yaml', 'yml'))],
                                            title='Selecteer een muziekbestand')
