# Henrik Eriksson 2003-11-17
# revision: Magnus Rosell 2006-08-10
# revision: Joel W m fl 2010-10-27
# revision: Linda 2011-09-27
# revision: Linda 2012-10-03 (Tkinter/tkinter)

from tkinter import *

# Ändrade till relevant version, samt ändra färg på text från vitt till svart


class Ruta:
    def __init__(self, atom="()", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None


class Molgrafik:

    def __init__(self):
        self.root = None
        self.stor = ("Courier", 18, "bold")
        self.liten = ("Courier", 14, "bold")

    def ram(self, master, sidan):
        ramen = Frame(master, bg="white")
        ramen.pack(side=sidan, fill=BOTH)
        return ramen

    def atomruta(self, master, namn, num):
        ruta = Frame(master, bg="yellow", borderwidth=2, relief=GROOVE)
        ruta.pack(side=LEFT)
        atom = Frame(ruta, bg="yellow")
        atom.pack(side=LEFT)
        Label(atom, text=namn, font=self.stor, bg="yellow", fg="black").pack()  # Svart textfärg
        Frame(atom, height=5, bg="yellow").pack()
        if num > 1:
            Label(ruta, text=str(num), font=self.liten, bg="yellow", fg="black").pack(side=BOTTOM)  # Svart textfärg

    def streck(self, master):
        strecket = Frame(master)
        strecket.pack(side=LEFT, fill=BOTH, expand=True)
        Frame(strecket, bg="white", height=20).pack(fill=X)
        Frame(strecket, bg="red", height=4, width=25).pack(fill=X)
        Frame(strecket, bg="white").pack(fill=BOTH, expand=1)

    def stolpe(self, master):
        hela = self.ram(master, TOP)
        stolpen = self.ram(hela, LEFT)
        Frame(stolpen, bg="white", width=15).pack(side=LEFT)
        Frame(stolpen, bg="red", width=4, height=25).pack(side=LEFT)
        Frame(hela, bg="white").pack(fill=BOTH, expand=1)

    def picture(self, master, p):
        if p is None: return
        storruta = self.ram(master, LEFT)
        rest = self.ram(master, LEFT)
        uppruta = self.ram(storruta, TOP)
        nerruta = self.ram(storruta, TOP)
        self.atomruta(uppruta, p.atom, p.num)
        if p.down:
            self.stolpe(nerruta)
            self.picture(nerruta, p.down)
            self.ram(nerruta, TOP)
        if p.next:
            self.streck(uppruta)
            self.picture(rest, p.next)

    def show(self, p):
        # Kontrollera om ett Tkinter-fönster redan existerar. Om ja, förstör det för att starta om.
        if self.root is not None:
            self.root.destroy()

        # Skapa ett nytt Tkinter-huvudfönster.
        self.root = Tk()

        # Skapa en label i huvudfönstret. Denna label är egentligen bara ett utrymme
        # och används inte för att visa någon text. Den hjälper till att styra layouten.
        Label(self.root, text="  ", font=self.stor, bg="white").pack(side=LEFT, fill=Y)

        # Anropa picture-metoden med det nya fönstret och det första Ruta-objektet (p).
        # Denna metod kommer att hantera skapandet av den grafiska representationen av molekylen.
        self.picture(self.root, p)

        # Starta Tkinter-händelseloopen. Detta håller fönstret öppet och väntar på händelser
        # (som knapptryckningar, fönsterstängning, etc.) för att hantera dem. Händelseloopen
        # fortsätter tills användaren stänger fönstret.
        mainloop()

