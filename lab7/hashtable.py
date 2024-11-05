class HashNode:
    """Noder till klassen Hashtable """

    def __init__(self, key="", data=None):
        """key är nyckeln som används vid hashningen
        data är det objekt som ska hashas in"""
        self.key = key
        self.data = data

    def __str__(self):
        return str(self.data)


class Hashtable:

    def __init__(self, size):
        """size: hashtabellens storlek"""
        self.size = size
        self.table = [[] for _ in range(self.size)] #tabell där varje element i tabellen är en tom lista.

    def store(self, key, data):
        """key är nyckeln
        data är objektet som ska lagras
        Stoppar in "data" med nyckeln "key" i tabellen."""
        index = self.hashfunction(key)
        # Gå igenom krocklistan för att se om nyckeln redan finns
        for node in self.table[index]:
            if node.key == key:
                node.data = data  # Om nyckeln redan finns, uppdatera datan
                return
        # Om nyckeln inte finns, lägg till en ny nod i krocklistan
        self.table[index].append(HashNode(key, data))

    def search(self, key):
        """key är nyckeln
        Hämtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
        Om "key" inte finns ska det bli KeyError """
        index = self.hashfunction(key)
        for node in self.table[index]:
            if node.key == key:
                return node.data
        raise KeyError("Nyckeln finns inte i hashtabellen.")

    def hashfunction(self, key):
        """key är nyckeln
        Beräknar hashfunktionen för key med en modifierad version för att minska kollisioner"""
        prime = 457  # Primtalet för att minska risken för kollisioner
        hash_val = hash(key) + prime
        return hash_val % self.size