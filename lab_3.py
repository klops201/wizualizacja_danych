#zad1.
print('------zadanie 1------')
a = [1-x for x in range(11)]
b = [4**x for x in range(8)]
c = [x for x in b if x % 2 == 0]
print(a)
print(b)
print(c)
print('\n\n')


#zad3.
print('------zadanie 3------')
zakupy = {'konserwa': 'sztuki', 'banany': 'kg', 'kartacz': 'sztuki', 'ziemniaki': 'kg'  }
tylko_sztuki = [k for (k,v) in zakupy.items() if 'sztuki' in v]
print(tylko_sztuki)
print('\n\n')


#zad4.
print('------zadanie 4------')
def czy_prostok(a,b,c):
    prost = 0

    if (a == b) & (b == c):
        print('trojkat jest rownoboczny, zatem')

    elif (a > b) & (a > c):
        if b * b + c * c == a * a:
            prost = 1

    elif (b > a) & (b > c):
        if a * a + c * c == b * b:
            prost = 1

    elif (c > b) & (c > a):
        if b * b + a * a == c * c:
            prost = 1


    if prost == 1:
        return print('trojkat jest prostokatny')
    else:
        return print('trojkat nie jest prostokatny')

print(czy_prostok(5,10,4))
print(czy_prostok(5,5,5))
print(czy_prostok(5,3,4))
print('\n\n')

#zad5.
print('------zadanie 5------')
def pole_t(a = 2,b = 4,h = 6):
    p = (a + b) * h/ 2
    return p

print(pole_t())
print('\n\n')

#zad6.
print('------zadanie 6------')
def ciag_mno(a =1 ,b = 4,ile = 10):
    iloczyn = 1

    for x in range(1, ile + 1):
     iloczyn *=  a * pow(b, x-1)

    return iloczyn

print(ciag_mno())
print('\n\n')
