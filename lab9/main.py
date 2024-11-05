from sys import stdin
from linkedQFile import *


class Syntaxfel(Exception):
    pass


VALID_ATOMS = {
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al",
    "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe",
    "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr",
    "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm",
    "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W",
    "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
    "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf",
    "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
}


def read_molecule(queue):
    if queue.peek() == '(':
        queue.dequeue()
        read_mol(queue)
        if queue.peek() != ')':
            raise Syntaxfel("Saknad högerparentes vid radslutet" + queue_to_string(queue))
        queue.dequeue()  # Ta bort högerparentesen
        read_num(queue)
    else:
        read_group(queue)


def read_mol(queue):
    if queue.is_empty() or queue.peek() == ')':
        raise Syntaxfel("Felaktig gruppstart vid radslutet " + queue_to_string(queue))

    if queue.is_empty() or queue.peek().isdigit():
        # Om inmatning är en siffra
        num = queue.peek()
        raise Syntaxfel(f"Felaktig gruppstart vid radslutet {num}")

    while not queue.is_empty() and queue.peek() not in (')', '#'):
        read_molecule(queue)


def read_group(queue):
    read_atom(queue)
    if not queue.is_empty() and queue.peek().isdigit():
        read_num(queue)


def read_atom(queue):
    atom = read_LETTER(queue)
    atom = read_letter(queue, atom)

    if atom not in VALID_ATOMS:
        raise Syntaxfel("Okänd atom vid radslutet " + queue_to_string(queue))

    return atom


def read_LETTER(queue):
    ch = queue.peek()

    if ch is None or not ch.isupper():
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + queue_to_string(queue))
    atom = queue.dequeue()

    return atom


def read_letter(queue, atom):
    if not queue.is_empty() and queue.peek().islower():
        atom += queue.dequeue()
    return atom


def read_num(queue):
    num_str = ''
    while not queue.is_empty() and queue.peek().isdigit():
        num_str += queue.dequeue()

    if not num_str:
        raise Syntaxfel("Saknad siffra vid radslutet " + queue_to_string(queue))

    num = int(num_str)

    if num_str.startswith('0') and len(num_str) > 1:
        raise Syntaxfel(f"För litet tal vid radslutet {num}" + queue_to_string(queue, True))
        # raise Syntaxfel("För litet tal vid radslutet" + f"{num}" + queue_to_string(queue, True))
        # Tidigare fel från unittest

    # Lösning för problemet för inmatningsrad 7 (H02C)
    # 0 och 2 dequeue-as och tas bort från kön, vilket var ett problem
    # det skrevs endast C ut på rad 87 med queue_to_string
    # löstes genom att lägga till if satsen: if num_str.startswith('0') and len(num_str) > 1...

    if num_str.startswith('0') or num < 2:
        raise Syntaxfel("För litet tal vid radslutet " + queue_to_string(queue, True))


def queue_to_string(queue, dequeue_all=False):
    result = ''
    copy = queue.first
    while copy:
        result += copy.value
        if dequeue_all:
            queue.dequeue()  # Det här ändrar kön i realtid om dequeue_all är sant
        copy = copy.next
    return result.strip('#')


def check_molecule(molecule):
    queue = LinkedQueue()
    for char in molecule + '#':  # Lägg till ett stopptecken för att märka slutet av formeln
        queue.enqueue(char)
    try:
        read_mol(queue)
        if queue.peek() != '#':  # Check for the end marker
            raise Syntaxfel("Felaktig gruppstart vid radslutet " + queue_to_string(queue))
    except Syntaxfel as error:
        return str(error)
    return "Formeln är syntaktiskt korrekt"


def main():
    for line in stdin:
        molecule = line.strip()
        if molecule == '#':
            break  # Avslutar läsningen när # tecken upptäcks
        result = check_molecule(molecule)
        print(result)


if __name__ == "__main__":
    main()
