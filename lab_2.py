import sys as system
#Zad 1. Napisz skrypt, w którym tworzysz listę ulubionych sportów,
# odwróć ją a następnie dodaj mniej lubiane sporty na sam koniec.
print('------zadanie 1------')
sporty = ['pilka nozna', 'silownia', 'bieganie', 'badminton']
print(sporty)
sporty.reverse()
print(sporty)
sporty.extend(('koszykowka', 'wedkarstwo', 'kajakarstwo'))
print(sporty)
print('\n\n')

#Zad 2. Stwórz słownik skrótów powszechnie używanych w gazetach lub artykułach internetowych.
print('------zadanie 2------')
slownik = {'zw': 'zaraz wracam', 'jj': 'juz jestem', 'm.in.': 'miedzy innymi', 'nk': 'niech ktos'}
print(slownik)
print('\n\n')

#Zad 3. Stwórz słownik z ulubionymi grami komputerowymi.Policz liczbę elementów w słowniku.
print('------zadanie 3------')
s_gry = {'gta': 'grand theft auto', 'cs': 'counter-strike', 'mc': 'minecraft', 'ets2': 'euro truck simulator2'}
print(s_gry)
print('liczba gier: ', sum(value != 0 for value in s_gry.values()))
print('\n\n')

#Zad 4. Napisz skrypt, który pobiera od użytkownika zdanie i liczy wystąpienia litery a. Użyj funkcji input
print('------zadanie 4------')
napis = input('podaj dowolne zdanie w którym wystepuje przynajmniej raz "a": ')
print('podane zdanie: ', napis)
print('"a" w zdaniu pojawilo sie ', napis.count('a'), ' razy')
print('\n\n')

#Zad 5. Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz obliczenia: ab + c.
#Użyj instrukcji readline() i write()).
print('------zadanie 5------')
system.stdout.write('podaj pierwsza liczbe calkowita: ')
a = system.stdin.readline()
system.stdout.write('podaj druga liczbe calkowita: ')
b = system.stdin.readline()
system.stdout.write('podaj trzecia liczbe calkowita: ')
c = system.stdin.readline()
a = int(a)
b = int(b)
c = int(c)
wynik = a**b+c
wynik = str(wynik)
system.stdout.write(' a^b + c = ')
system.stdout.write(wynik)
print('\n\n')

# Zad 6. Wczytaj trzy liczby całkowite a,b,c i sprawdź, która z nich jest największa.
# W zależności od wyniku wyświetl odpowiedni komunikat.Użyj zagnieżdżeń.
print('------zadanie 6------')
x = input('podaj pierwsza liczbe calkowita: ')
y = input('podaj druga liczbe calkowita: ')
z = input('podaj trzecia liczbe calkowita: ')
x = int(x)
y = int(y)
z = int(z)

if (x == y) & (y == z):
    print('wszystkie podane liczby sa rowne')

elif (x >= y) & (x >= z):
        if (x == y) | (x == z):
            print('sa 2 najwieksze liczby')
        else:
            print('liczba ' + str(x) + ' jest najwieksza')

elif (y >= z) & (y >= x):
    if (y == z) | (y == x):
        print('sa 2 najwieksze liczby')
    else:
        print('liczba ' + str(y) + ' jest najwieksza')

else:
    if (z == y) | (z == x):
        print('sa 2 najwieksze liczby')
    else:
        print('liczba ' + str(z) + ' jest najwieksza')
print('\n\n')

# Zad 7. Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float.
# Następnie za pomocą użycia pętli for podnieś każdą liczbę do kwadratu.
print('------zadanie 7------')
lista = [5, 6.66, 10, 9.99]
for x in lista:
    x = x*x
    print(x)
print('\n\n')

# Zad 8. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb,
# następnie dodaje do listy tylko parzyste liczby.
print('------zadanie 8------')
i = 0
liczby = []
while i != 10:
    k = input('podaj liczbe calkowita: ')
    k = int(k)
    if k % 2 == 0:
        liczby.append(k)
    i += 1
print(liczby)
print('\n\n')

# Zad 9. Napisz skrypt, który rysuje następującą literę.
# EEEEEE
# E
# EEEEEE
# E
# EEEEEE
print('------zadanie 9------')
print('tego zadania nie potrafie zrobic')
print('\n\n')

# Zad. 10 Napisz skrypt, który liczy pierwiastek z liczby podanej przez użytkownika
# jeśli użytkownik poda wartość ujemną to powinien być wyłapany błąd.
print('------zadanie 10------')
import math
x = input('podaj liczbe z jakiej ma byc obliczony pierwiastek: ')
x = int(x)
if x < 0:
    print('nie mozna obliczyc pierwiastka z liczby ujemnej')
print('pierwiastek z ', x, ' = ', math.sqrt(x))
