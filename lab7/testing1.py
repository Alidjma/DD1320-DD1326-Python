class Drama:
    def __init__(self, name, rating, actors, viewship_rate, genre, director, writer, year, episodes, network):
        self.name = name
        self.rating = rating
        self.actors = actors
        self.viewship_rate = viewship_rate
        self.genre = genre
        self.director = director
        self.writer = writer
        self.year = year
        self.episodes = episodes
        self.network = network

    def __str__(self):
        return f"{self.name} ({self.year}) - {self.genre} - {self.rating}/10" \
               f"\nDirektör för serien är {self.director} och Writern är {self.writer}" \
               f"\nKända skådespelare i serien är {self.actors} " \
               f"\nÖvrig information:" \
               f"\nTittarantal: {self.viewship_rate}, Avsnitt: {self.episodes}. Sänds på: {self.network}"

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
        self.table = [[] for _ in range(self.size)]

    def store(self, key, data):
        index = self.hashfunction(key)
        for node in self.table[index]:
            if node.key == key:
                node.data = data
                return
        self.table[index].append(HashNode(key, data))

    def search(self, key):
        index = self.hashfunction(key)
        for node in self.table[index]:
            if node.key == key:
                return node.data
        raise KeyError("Nyckeln finns inte i hashtabellen.")

    def hashfunction(self, key):
        """key är nyckeln
        Beräknar hashfunktionen för key med en modifierad version för att minska kollisioner"""
        prime = 19  # Primtalet för att minska risken för kollisioner
        hash_val = hash(key) + prime
        return hash_val % self.size


if __name__ == "__main__":
    hashtable = Hashtable(457)  # Skapar en hashtabell med en storlek av 19

    with open("kdramaMini.txt", "r", encoding="utf-8") as file:
        next(file)  # Ignorera första raden (header)
        for line in file:
            parts = line.strip().split(',')
            drama = Drama(*parts)
            hashtable.store(drama.name, drama)

    drama_name = input("Ange namnet på det drama du vill söka efter: ")
    try:
        found_drama = hashtable.search(drama_name)
        print(found_drama)
    except KeyError:
        print(f"{drama_name} finns inte i hashtabellen.")
