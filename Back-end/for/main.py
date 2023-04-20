from helpers import get_countries
import re

""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """

# Order the countries by length to see which are the shortest
countries = get_countries()

# Functions

# 1.


def shortest_names(countries):
    short_names = []
    for country in countries:
        if len(country) == 4:
            short_names.append(country)
    print(short_names)


shortest_names(countries)


# 2.

def most_vowels(countries):

    countryVowelsAmount = []

    for nation in countries:
        countryVowelsAmount.append(
            {"nation": nation, "Vowel Amount": len(re.sub("[^aeiou]", "", nation))}
        )

    countryVowelsAmountSorted = sorted(
        countryVowelsAmount, key=lambda i: i["Vowel Amount"], reverse=True
    )
    print(
        "Countries with the highest number of vowels: ",
        countryVowelsAmountSorted[0],
        countryVowelsAmountSorted[1],
        countryVowelsAmountSorted[2],
    )


most_vowels(countries)


# 3.

def alphabet_set(countries):
    alphabetCountries = []
    alphabet = [
        "a", "b", "c", "d", "e", "f", "g",
        "h", "i", "j", "k", "l", "m", "n",
        "o", "p", "q", "r", "s", "t", "u",
        "v", "w", "x", "y", "z",
    ]

    for countryName in countries:
        for letter in alphabet:
            if letter in countryName:
                alphabetCountries.append(countryName)
                alphabet.remove(letter)

    alphabetCountries = list(dict.fromkeys(alphabetCountries))  # Remove duplicates

    print(
        "Collection of countries containing all the letters of the alphabet: ",
        alphabetCountries,
    )

    print("alphabet countries length:", len(alphabetCountries))


alphabet_set(countries)
