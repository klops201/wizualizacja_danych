# Zad1. Napisz pierwszy skrypt, w którym zadeklarujesz po dwie zmienne każdego typu a następnie wyświetl te zmienne
napis1,napis2= 'napis','testowy'
print('------zadanie 1------')
print(napis1)
print(napis2)
print(napis1+napis2)
wiek=20
print(wiek)

#Zad2. Stwórz skrypt kalkulator, w którym wykorzystać wszystkie podstawowe działania arytmetyczne
print('------zadanie 2------')
a,b,c= 1,2,3
print('a,b,c= 1,2,3')
dodawanie=a+b
print('a+b=',dodawanie)
odejmowanie=b-a
print('b-a=',odejmowanie)
mnozenie=b*a
print('b*a=',mnozenie)
dzielenie=c/a
print('c/a=',dzielenie)
potegowanie=b**c
print('b**c=',potegowanie)
modulo=c%b
print('c%b=',modulo)

#zad3.Napisz skrypt, w którym stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %
print('------zadanie 3------')
a=3
a+=1 ; print(a)
a-=1 ; print(a)
a*=2 ; print(a)
a/=2 ; print(a)
a**=2 ; print(a)
a%=5 ; print(a)

#Zad4. Napisz skrypt, który policzy i wyświetli następujące wyrażenia
print('------zadanie 4------')
import math
print('a)')
print (math.e**10)
print('b)')
print((math.log(5+(math.sin(8)**2)))**(1/6))
print('c)')
print(math.floor(3.55))
print('d)')
print(math.ceil(4.80))

#Zad.5 Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie wielkimi literami.
# Użyj odpowiedniej metody by wyświetlić je pisane tak, że pierwsza litera jest wielka a poszostałe małe.
print('------zadanie 5------')
a='BARTOSZ'
b='OSTROKOLOWICZ'
print(a.capitalize(),b.capitalize())

#Zad.6 Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z powtarzającymi się słowami np. „la la la”.
# Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”.
print('------zadanie 6------')
txt='la la pioseneczka la la'
print(txt.count('la'))

#Zad.7 Zapisz dowolną zmienną łańcuchową i wyświetl jej drugą i ostatnią literę, wykorzystując indeksy.
print('------zadanie 7------')
a='napis'
print(a[1],a[4])

#Zad.8 Zmienne łańcuchowe możemy dzielić wykorzystaj zmienną z Zad. 6 i spróbuj ją podzielić na poszczególne wyrazy.
print('------zadanie 8------')
print(txt.split())

#Zad.9 Napisz skrypt, w którym zadeklarujesz zmienne typu: string, float i szestnastkowe.
# Następnie wyświetl je wykorzystując odpowiednie formatowanie.
print('------zadanie 9------')
a='zmienna typu string'
b=20.21
c=hex(2021)
print(a)
print(b)
print(c)