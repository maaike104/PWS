from Tkinter import Tk, Frame, Button, Label

from bestand import Bestand
from machine import Machine


class Scherm:
    def __init__(self, app):
        self.bestandskiezer = Bestand()
        self.scherm = Frame(app)
        self.scherm.pack()
        self.kiesknop = Button(self.scherm, text='Kies muziekbestand',
                               command=self.kies_bestand)
        self.afspeelknop = Button(self.scherm, text='Afspelen', command=self.speel_af)
        self.afsluitknop = Button(self.scherm, text='Afsluiten', command=quit)
        self.tekst = Label(self.scherm, width=50, text='Geen bestand geselecteed!')

        self.kiesknop.pack()
        self.tekst.pack()
        self.afspeelknop.pack()
        self.afsluitknop.pack()

    def kies_bestand(self):
        self.bestandskiezer.selecteer_bestand()
        self.tekst['text'] = self.bestandskiezer.bestandsnaam

    def speel_af(self):
        if self.bestandskiezer.bestandsnaam:
            machine = Machine(self.bestandskiezer.bestandsnaam)
            machine.afspelen()
        else:
            self.tekst['text'] = 'Geen bestand geselecteerd!'


if __name__ == '__main__':
    app = Tk()
    scherm = Scherm(app)
    app.mainloop()
