#napisz funkcję, która sprawdza, czy dany wyraz jest palindromem czyli
#czytany od lewej do prawej i od prawej do lewej brzmi tak samo.
#Zaprogramuj funkcję, która przyjmuje jeden argument (typu string) 
# i zwraca wartość boolean: True/False, mówiącą czy podany tekst jest palindromem.
#Pamiętaj, że string/tekst, to kolekcja znaków. 
# Znasz już funkcje kolekcji, które pozwalają odnosić się do elementów indeksowanych od początku i od końca.
#Do zadania dodaj krótką dokumentację i umieść je w zdalnym repozytorium. Link prześlij Mentorowi.

import re
def czy_palindrom(word):
    """
    Checks if a word is a palindrome.
    """
    only_letters = re.sub("[^a-zA-Z]","",word)
    return only_letters.lower() == only_letters.lower()[::-1]
    

czy_palindrom(" ,.,$kot toK.")
