class DictHash:
    def __init__(self):
        self._dict = {}

    def store(self, key, value):
        self._dict[key] = value

    def search(self, key):
        return self._dict.get(key, None)

    def __getitem__(self, key):
        return self.search(key)

    def __contains__(self, key):
        return key in self._dict

    def __str__(self):  # Ny metod för att skriva ut innehållet
        return str(self._dict)


class Drama:
    def __init__(self, namn, rating, actors, viewship_rate, genre, director, writer, year, episodes, network):
        self.namn = namn
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
        return f"{self.namn}: {self.rating}/10, Actors: {self.actors}, Genre: {self.genre}, Year: {self.year}"


def las_in_kdrama_från_fil(filnamn):
    dramas = []
    with open(filnamn, 'r', encoding='utf-8') as file:
        next(file)  # Skip the header
        for line in file:
            namn, rating, actors, viewship_rate, genre, director, writer, year, episodes, network = line.strip().split(',')
            drama = Drama(namn.lower(), rating, actors, viewship_rate, genre, director, writer, year, episodes, network)
            dramas.append(drama)
    return dramas


d = DictHash()

dramas = las_in_kdrama_från_fil("kdramaMini.txt")

for drama in dramas:
    print(drama)  # Skriv ut varje drama för att verifiera inläsningen
    d.store(drama.namn, drama)

print("\nInnehåll i DictHash:")
print(d)  # Skriv ut innehållet i DictHash för att verifiera lagringen

# Fråga användaren om input
sokt_drama_namn = input("\nAnge namnet på det drama du vill söka efter: ").lower()

try:
    print(d[sokt_drama_namn])
except KeyError:
    print(f"{sokt_drama_namn} finns inte i hashtabellen.")