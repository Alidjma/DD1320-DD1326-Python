from bintreeFile import Bintree
from linkedQFile import LinkedQ

svenska = Bintree()  # Här lägger vi in alla ord, inga kopior
gamla = Bintree()  # Här lägger vi in 'dumbarn' dvs kopiorna
q = LinkedQ()


class ParentNode:
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent

    def write_chain(self, child):
        if child is not None:
            self.write_chain(child.parent)
            print(child.word)


class SolutionFound(Exception):
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


def makechildren(node):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

    for i in range(len(node.word)):
        for bokstav in alfabet:
            nytt_ord = list(node.word)
            nytt_ord[i] = bokstav
            nytt_ord = ''.join(nytt_ord)
            if svenska.__contains__(nytt_ord) and not gamla.__contains__(nytt_ord):
                child_node = ParentNode(nytt_ord, parent=node)
                gamla.put(nytt_ord)
                q.enqueue(child_node)


def main():
    read_file()
    startord = input("Ange startord: ")
    slutord = input("Ange slutord: ")
    start_node = ParentNode(startord)
    q.enqueue(start_node)  # lägger in ParentNode som stamfader i kön
    gamla.put(startord)  # Lägger in stamfadern i sökträd för kopior
    try:
        while not q.isEmpty():
            word_node = q.dequeue()  # En 'ParentNode' läggs till i kön
            makechildren(word_node)  # skapar alla dess barn
            if word_node.word == slutord:
                print("\nVägen från", startord, "är:")
                word_node.write_chain(word_node)
                raise SolutionFound()  # Om någon av barnen är lösningen, raise exception
        print("Det finns ingen väg")
    except SolutionFound:
        print()


main()
