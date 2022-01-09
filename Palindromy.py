#napisz funkcję, która sprawdza, czy dany wyraz jest palindromem czyli
#czytany od lewej do prawej i od prawej do lewej brzmi tak samo.
#Zaprogramuj funkcję, która przyjmuje jeden argument (typu string) 
# i zwraca wartość boolean: True/False, mówiącą czy podany tekst jest palindromem.
#Pamiętaj, że string/tekst, to kolekcja znaków. 
# Znasz już funkcje kolekcji, które pozwalają odnosić się do elementów indeksowanych od początku i od końca.
#Do zadania dodaj krótką dokumentację i umieść je w zdalnym repozytorium. Link prześlij Mentorowi.


def czy_palindrom(word):
    """
    Checks if a word is a palindrome.
    """
    lenght = len(word)
    if lenght % 2 != 0:
        lenght = lenght+1
    iterations_no = int(lenght/2)
    
    iloczyn = 1
    for i in range(0,iterations_no):
        if word[0+i] == word [-1-i]:
            result = 1
        else:
            result = 0
        iloczyn = iloczyn*result
    print(bool(iloczyn))
   

czy_palindrom("anna")
