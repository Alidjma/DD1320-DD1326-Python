from sys import stdin
from linkedQFile import *


class Syntaxfel(Exception):
    pass


def molekyl(queue):
    # Om det första tecknet inte är en versal (stor bokstav), ska det misslyckas här.
    if queue.is_empty() or not queue.peek().isupper():
        raise Syntaxfel(f"Saknad stor bokstav vid radslutet {queue_to_string(queue)}")

    # Bearbeta en atom följt av ett valfritt tal.
    atom(queue)
    if not queue.is_empty() and queue.peek().isdigit():
        num(queue)
    # Om det finns något kvar i kön efter att ha bearbetat en atom och ett valfritt nummer, är det ett syntaxfel.
    if not queue.is_empty():
        raise Syntaxfel(f"Saknad stor bokstav vid radslutet {queue_to_string(queue)}")


def atom(queue):
    LETTER(queue)
    # Om nästa tecken är en gemen (liten bokstav), ska den vara en del av den aktuella atomen.
    if not queue.is_empty() and queue.peek().islower():
        letter(queue)
    # Efter en gemen ska det inte komma något eller ett tal bör följa.
    if not queue.is_empty() and not queue.peek().isdigit() and queue.peek().isupper():
        raise Syntaxfel(f"Saknad siffra vid radslutet {queue_to_string(queue)}")


def LETTER(queue):
    # Kolla om det nuvarande tecknet är en versal och avlägsna den från kön.
    ch = queue.peek()
    if ch is None or not ch.isupper():
        rest_of_queue = queue_to_string(queue)
        raise Syntaxfel(f"Saknad stor bokstav vid radslutet {rest_of_queue}")
    queue.dequeue()

    # Kontrollera att efter en versal kommer antingen en gemen eller ett tal, annars kasta ett syntaxfel.
    # (inga specialtecken)
    if not queue.is_empty() and not (queue.peek().islower() or queue.peek().isdigit()):
        rest_of_queue = ch + queue_to_string(queue)
        raise Syntaxfel(f"Felaktigt format efter stor bokstav vid radslutet {rest_of_queue}")


def letter(queue):
    # Kontrollera om det nuvarande tecknet är en gemen och avlägsna den från kön.
    ch = queue.peek()
    if ch is None or not ch.islower():
        raise Syntaxfel("Saknad liten bokstav vid radslutet")
    queue.dequeue()
    # Efter en gemen ska kön vara tom eller nästa tecken ska vara en siffra.
    if not queue.is_empty() and queue.peek().isalpha():
        raise Syntaxfel(f"Saknad siffra eller ny stor bokstav vid radslutet {queue_to_string(queue)}")


def num(queue):
    if queue.is_empty():
        raise Syntaxfel("För litet tal vid radslutet")

    number_str = ""
    while not queue.is_empty() and queue.peek().isdigit():
        number_str += queue.dequeue()

    if number_str == '0':  # Om numret är enbart '0'
        raise Syntaxfel("För litet tal vid radslutet")
    elif len(number_str) > 1 and number_str[0] == '0':  # Om numret börjar med '0'
        raise Syntaxfel(f"För litet tal vid radslutet {int(number_str)}")

    number = int(number_str)  # Konverterar strängen till ett heltal
    if number == 1:
        raise Syntaxfel("För litet tal vid radslutet")
    elif number < 2:
        raise Syntaxfel(f"För litet tal vid radslutet {number}")


def queue_to_string(queue):
    # Skapa en sträng av alla kvarvarande element i kön.
    remaining = ""
    while not queue.is_empty():
        remaining += queue.dequeue()
    return remaining


def check_molecule(molecule):
    # Skapa en kö och lägg till alla tecken i molekylen i kön.
    q = LinkedQueue()
    for char in molecule:
        q.enqueue(char)

    try:
        # Analysera molekylens struktur med hjälp av kön.
        molekyl(q)
        # Om det finns något kvar i kön efter analysen, kasta ett syntaxfel.
        if not q.is_empty():
            raise Syntaxfel(f"Saknad stor bokstav vid radslutet {queue_to_string(q)}")
        # Om allt är korrekt, returnera att formeln är syntaktiskt korrekt.
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as e:
        # Om ett Syntaxfel inträffar, returnera felmeddelandet.
        return str(e)


def main():
    # Läs in molekyler en efter en och kontrollera deras syntaktiska struktur.
    for molecule in stdin:
        molecule = molecule.strip()
        if molecule == "#":
            break
        print(check_molecule(molecule))


if __name__ == "__main__":
    main()