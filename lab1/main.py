# -*- coding: utf-8 -*-
import csv
import random


class Drama:
    def __init__(self, lista):
        # Initialiserar attributen för en dramaserie från en rad i CSV-filen.
        self.name = lista[0]
        self.rating = lista[1]
        self.actors = lista[2]
        self.viewership_rate = lista[3]
        self.genre = lista[4]
        self.director = lista[5]
        self.writer = lista[6]
        self.year = lista[7]
        self.episodes = lista[8]
        self.channel = lista[9]

    def __str__(self):
        # Returnerar en formaterad sträng för att representera dramaserien.
        return f'{self.name :<40}{self.rating :<20}{self.genre :<50}{self.year :<20}{self.episodes :<20}'

    def __lt__(self, other):
        # Definierar sortering av dramaserier efter betyg (rating) i fallande ordning.
        try:
            return float(self.rating) > float(other.rating)
        except ValueError:
            # If either rating is non-numeric, consider them equal for sorting purposes
            return False

    def introduce(self):
        # Presenterar information om dramaserien.
        print(
            f"The Korean drama: '{self.name}' consists of {self.episodes} episodes and is of the genres: '{self.genre}'. \n"
            f"The actors are: '{self.actors}' and its rating is: '{self.rating}'")

    def combined_score(self):
        # Beräknar ett nytt nyckeltal för att jämföra seriens populäritet.
        score = float(self.rating) * float(self.viewership_rate)
        print("Its score is given by the product of rating and viewership rate: "
              f"{self.rating} * {self.viewership_rate} = {score}\n")



def read_csv_file(file_path):
    # Läser från CSV-filen
    drama_list = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            # Skapar Drama-objekt för varje rad i CSV-filen och lägger till i listan.
            drama_object = Drama(row)
            drama_list.append(drama_object)

    return drama_list


def search_drama(drama_list, target_name):
    # Funktion som söker efter namn på drama-serie från listan
    for drama in drama_list:
        if drama.name.lower() == target_name.lower():
            return drama
    return None


def main():
    file_path = 'kdrama.csv'
    drama_objects = read_csv_file(file_path)

    # Sorterar dramaserierna efter betyg (rating) i fallande ordning.
    sorted_by_rating = sorted(drama_objects)

    # Väljer och sorterar slumpmässiga dramaserier och presenterar dem.
    selected_dramas = random.sample(drama_objects, 2)
    sorted_selected_dramas = sorted(selected_dramas)
    for drama in sorted_selected_dramas:
        drama.introduce()
        drama.combined_score()

    # Skriver ut alla dramaserier sorterade efter betyg (rating).
    for drama in sorted_by_rating:
        print(drama)

    # User-input för att ropa på sök funktion
    user_input = input("Enter the name of the drama you are looking for: ")
    found_drama = search_drama(drama_objects, user_input)

    if found_drama:
        print(f"The drama: '{user_input}' was found:")
        found_drama.introduce()
    else:
        print(f"The drama: '{user_input}' was not found.")

main()