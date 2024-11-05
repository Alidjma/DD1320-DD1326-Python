from bintreeFile import Bintree

svenska = Bintree()  # Här lägger vi in alla ord, inga kopior
gamla = Bintree()  # Här lägger vi in 'dumbarn' dvs kopiorna


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
                print(nytt_ord)
                gamla.put(nytt_ord)
    else:
        print("Det finns en väg!")


def main():
    read_file()
    startord = input("Ange startord: ")
    slutord = input("Ange slutord: ")
    gamla.put(startord)  # Lägger in stamfadern i sökträd för kopior
    makechildren(startord)


main()