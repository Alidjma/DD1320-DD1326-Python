from bintreeFile import Bintree
from linkedQFile import LinkedQ

svenska = Bintree()  # Här lägger vi in alla ord, inga kopior
gamla = Bintree()  # Här lägger vi in 'dumbarn' dvs kopiorna
q = LinkedQ()


class Klar(Exception):
    # Används vid särfallet: att man hittar slutordet, dvs finner en väg!
    # Funkar som Exception
    pass


def read_file():
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()  # Ett trebokstavsord per rad
            if ordet in svenska:
                gamla.put(ordet)
            else:
                svenska.put(ordet)  # in i sökträdet


def makechildren(ord):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

    for i in range(len(ord)):
        for bokstav in alfabet:
            nytt_ord = ord.replace(ord[i], bokstav)
            if svenska.__contains__(nytt_ord) and not gamla.__contains__(nytt_ord):
                q.enqueue(nytt_ord)
                gamla.put(nytt_ord)


def main():
    read_file()
    startord = input("Ange startord: ")
    slutord = input("Ange slutord: ")
    q.enqueue(startord)  # lägger in stamfader i kön
    gamla.put(startord)  # Lägger in stamfadern i sökträd för kopior
    try:
        while not q.isEmpty():
            word = q.dequeue()  # En 'word' är en node,
            makechildren(word)  # skapar alla dess barn
            if word == slutord:
                raise Klar(word)  # Om ngn av barnen är lösning, klart. Annars upprepa tills q blir tomt
        print("Det finns ingen väg")
    except Klar:
        print("Det finns en väg till", slutord)


main()