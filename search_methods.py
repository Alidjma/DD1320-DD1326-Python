import timeit


class Unique_track:
    def __init__(self, track_id, song_id, artist, title):
        self.track_id = track_id
        self.song_id = song_id
        self.artist = artist
        self.title = title

    def __lt__(self, other):
        return self.artist < other.artist


def binary_search(track_list, target):
    """ Tidskomplexitet O(logn)"""
    left, right = 0, len(track_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if track_list[mid].artist == target:
            return target  # Returnera den sökta strängen om den hittades.
        elif track_list[mid].artist < target:
            left = mid + 1
        else:
            right = mid - 1

    return None  # Returnera None om strängen inte finns i listan.


def get_artist_name(dictionary, key):
    """ Tidskomplexitet O(1) i bästa fall, sämsta O(n) om hash-kollisioner uppstår"""
    return dictionary.get(key)


def readfile():
    track_list = []
    track_dict = {}

    with open("unique_tracks.txt", "r", encoding="utf-8") as file:
        for row in file:
            fixed_row = row.strip('\n').split('<SEP>')
            track_object = Unique_track(fixed_row[0], fixed_row[1], fixed_row[2], fixed_row[3])
            track_list.append(track_object)
            track_dict[fixed_row[2]] = track_object

    return track_list, track_dict


def linsok(track_list, target_artist):
    """ Tidskomplexitet O(n) """
    for x in track_list:
        if x.artist == target_artist:
            return x
    return False


def main():
    lista, dictionary = readfile()
    #n = len(lista)
    #n = 500000
    n = 250000
    print("Antal element =", n)

    #sista = lista[n - 1]
    #testartist = sista.artist
    testartist = lista[-1].artist

    linjtid = timeit.timeit(stmt=lambda: linsok(lista, testartist), number=10000)
    print("Linjärsökningen tog", round(linjtid, 4), "sekunder")

    sorterad_lista = sorted(lista)
    bintid = timeit.timeit(stmt=lambda: binary_search(sorterad_lista, testartist), number=10000)
    print("Binärsökningen tog", round(bintid, 4), "sekunder")

    hashtid = timeit.timeit(stmt=lambda: get_artist_name(dictionary, testartist), number=10000)
    print("Sökning i hashtabell tog", round(hashtid, 4), "sekunder")


main()