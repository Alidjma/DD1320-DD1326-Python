from sys import stdin
from linkedQFile import LinkedQueue
from molgrafik import Molgrafik


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


ATOMIC_WEIGHTS = {
    "H": 1.00794, "He": 4.002602, "Li": 6.941, "Be": 9.012182, "B": 10.811,
    "C": 12.0107, "N": 14.0067, "O": 15.9994, "F": 18.9984032, "Ne": 20.1797,
    "Na": 22.98976928, "Mg": 24.3050, "Al": 26.9815386, "Si": 28.0855, "P": 30.973762,
    "S": 32.065, "Cl": 35.453, "K": 39.0983, "Ar": 39.948, "Ca": 40.078,
    "Sc": 44.955912, "Ti": 47.867, "V": 50.9415, "Cr": 51.9961, "Mn": 54.938045,
    "Fe": 55.845, "Co": 58.933195, "Ni": 58.6934, "Cu": 63.546, "Zn": 65.38,
    "Ga": 69.723, "Ge": 72.64, "As": 74.92160, "Se": 78.96, "Br": 79.904,
    "Kr": 83.798, "Rb": 85.4678, "Sr": 87.62, "Y": 88.90585, "Zr": 91.224,
    "Nb": 92.90638, "Mo": 95.96, "Tc": 98, "Ru": 101.07, "Rh": 102.90550,
    "Pd": 106.42, "Ag": 107.8682, "Cd": 112.411, "In": 114.818, "Sn": 118.710,
    "Sb": 121.760, "I": 126.90447, "Te": 127.60, "Xe": 131.293, "Cs": 132.9054519,
    "Ba": 137.327, "La": 138.90547, "Ce": 140.116, "Pr": 140.90765, "Nd": 144.242,
    "Pm": 145, "Sm": 150.36, "Eu": 151.964, "Gd": 157.25, "Tb": 158.92535,
    "Dy": 162.500, "Ho": 164.93032, "Er": 167.259, "Tm": 168.93421, "Yb": 173.054,
    "Lu": 174.9668, "Hf": 178.49, "Ta": 180.94788, "W": 183.84, "Re": 186.207,
    "Os": 190.23, "Ir": 192.217, "Pt": 195.084, "Au": 196.966569, "Hg": 200.59,
    "Tl": 204.3833, "Pb": 207.2, "Bi": 208.98040, "Po": 209, "At": 210,
    "Rn": 222, "Fr": 223, "Ra": 226, "Ac": 227, "Th": 232.03806, "Pa": 231.03588,
    "U": 238.02891, "Np": 237, "Pu": 244, "Am": 243, "Cm": 247, "Bk": 247,
    "Cf": 251, "Es": 252, "Fm": 257, "Md": 258, "No": 259, "Lr": 262,
    "Rf": 265, "Db": 268, "Sg": 271, "Bh": 272, "Hs": 270, "Mt": 276,
    "Ds": 281, "Rg": 280, "Cn": 285
}


class Ruta:
    # Klassen initierarr en atom eller en grupp av atomer i en molekyl.
    def __init__(self, atom="()", num=1):
        self.atom = atom
        self.num = num
        self.next = None  # Referens till nästa atom/grupp i molekylen.
        self.down = None  # Referens till en nedåtriktad grupp (i parenteser).


def read_group(queue):
    # Läser en grupp atomer från kön och skapar en Ruta-instans för den.
    rutan = Ruta()
    if queue.peek() == '(':
        # Om gruppen startar med '(', hantera det som en nedåtriktad grupp.
        queue.dequeue()
        rutan.down = read_mol(queue)  # Läser molekyl inom parenteser.
        if queue.peek() != ')':
            raise Syntaxfel("Saknad högerparentes vid radslutet " + queue_to_string(queue))
        queue.dequeue()
        rutan.num = read_num(queue)  # Läs numret efter parenteser.
    else:
        rutan.atom = read_atom(queue)  # Läs atomnamnet.
        if not queue.is_empty() and queue.peek().isdigit():
            rutan.num = read_num(queue)
    return rutan


def read_mol(queue):
    # Läser en molekyl och bygger upp en kedja av Ruta-instanser.
    start = Ruta()
    mol = start
    while not queue.is_empty() and queue.peek() not in (')', '#'):
        mol.next = read_group(queue)  # Läs nästa grupp och koppla till kedjan.
        mol = mol.next
    return start.next


def read_atom(queue):
    # Läser en atom från kön. Först en stor bokstav och sedan en liten bokstav om den finns.
    atom = read_LETTER(queue)
    atom = read_letter(queue, atom)
    # Kontrollerar om den lästa atomen finns i listan över giltiga atomer.
    if atom not in VALID_ATOMS:
        raise Syntaxfel("Okänd atom vid radslutet " + queue_to_string(queue))
    return atom


def read_LETTER(queue):
    # Kontrollerar och läser en stor bokstav från kön.
    ch = queue.peek()
    if ch is None or not ch.isupper():
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + queue_to_string(queue))
    return queue.dequeue()  # Tar bort och returnerar elementet från kön.


def read_letter(queue, atom):
    # Läser en liten bokstav om den finns och lägger till den till atomsträngen.
    if not queue.is_empty() and queue.peek().islower():
        atom += queue.dequeue()
    return atom


def read_num(queue):
    # Läser och returnerar ett tal från kön.
    num_str = ''
    while not queue.is_empty() and queue.peek().isdigit():
        num_str += queue.dequeue()
        # Kontrollerar om det finns ett tal och om det är giltigt.
    if not num_str:
        raise Syntaxfel("Saknad siffra vid radslutet " + queue_to_string(queue))
    num = int(num_str)
    if num_str.startswith('0') or num < 2:
        raise Syntaxfel("För litet tal vid radslutet " + queue_to_string(queue))
    return num


def queue_to_string(queue):
    # Konverterar innehållet i kön till en sträng.
    result = ''
    copy = queue.first
    while copy:
        result += copy.value  # Lägger till varje element i kön till strängen.
        copy = copy.next
    return result.strip('#')  # Tar bort stopptecknet '#' från slutet av strängen.


def check_molecule(molecule):
    # Kontrollerar syntaktisk korrekthet av en molekylformel.
    queue = LinkedQueue()
    for char in molecule + '#':
        queue.enqueue(char)
    try:
        mol = read_mol(queue)  # Läser och bygger ett syntaxträd för molekylen.
        if queue.peek() != '#':  # Kontrollerar om hela formeln har lästs korrekt.
            raise Syntaxfel("Felaktig gruppstart vid radslutet " + queue_to_string(queue))
    except Syntaxfel as error:
        return str(error), None
    return "Formeln är syntaktiskt korrekt", mol


def weight(mol):
    # Beräknar molekylvikten av en molekyl representerad av ett syntaxträd.
    if mol is None:
        return 0
    weight_sum = 0
    # Om den aktuella noden (Ruta) representerar en atom, lägg till dess vikt.
    if mol.atom != "()":
        weight_sum += ATOMIC_WEIGHTS[mol.atom] * mol.num  # Vikten av atomen multipliceras med antalet.
        # Adderar rekursivt vikten av nästa atom i kedjan och eventuella underkedjor.
    weight_sum += weight(mol.next)  # Addera vikten av nästa atom i molekylen.
    weight_sum += weight(mol.down)  # Addera vikten av eventuella undergrupper (inom parenteser).
    return weight_sum  # Returnera den totala vikten av molekylen.


def main():
    # Läser in molekylformler från standardinput och bearbetar dem.
    for line in stdin:
        molecule = line.strip()
        if molecule == '#':
            break
        result, mol = check_molecule(molecule)
        print(result)
        if mol:  # Om en giltig molekylstruktur (syntaxträd) skapades, visa den och beräkna dess vikt.
            mg = Molgrafik()  # Skapar ett nytt Molgrafik-objekt.
            mg.show(mol)  # Visar molekylstrukturen grafiskt.
            print("Molekylvikt:", weight(mol))

# VID START AV KOD VISA GRAFIK, STÄNG FÖNSTER - LÄS VIKT, SKRIV NÄSTA MOLEKYL OCH TRYCK # NÄR DU ÄR KLAR!

if __name__ == "__main__":
    main()
