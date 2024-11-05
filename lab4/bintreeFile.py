class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Bintree:
    def __init__(self):
        self.root = None

    def put(self, newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root, newvalue)

    def __contains__(self, value):
        # True om value finns i trädet, False annars
        return finns(self.root, value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")


def putta(p, newvalue):
    # Funktion som gör själva jobbet att stoppa in en ny nod
    # p är referens till existerande nod
    if p is None:
        return Node(newvalue)   # skapar ny nod med ny värde

    elif newvalue > p.value:
        p.right = putta(p.right, newvalue)  # insätter newvalue i höger subtree

    elif newvalue < p.value:
        p.left = putta(p.left, newvalue)    # insätter newvalue i vänster subtree

    return p


def finns(p, value):
    # Funktion som gör själva jobbet att söka efter ett värde
    if p is None:
        return False    # om värdet inte hittas

    elif value == p.value:
        return True     # om värdet hittas

    elif value < p.value:
        return finns(p.left, value)     # söker i vänstra subtree

    else:
        return finns(p.right, value)    # söker i högra subtree


def skriv(p):
    # Funktion som gör själva jobbet att skriva ut trädet
    if p is not None:
        skriv(p.left)
        print(p.value, end=" ")
        skriv(p.right)
