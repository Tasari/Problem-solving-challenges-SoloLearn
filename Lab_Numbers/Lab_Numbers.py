'''
Lab Numbers

A lab number is a number such that the square of any of its prime divisors is still one of its divisors.

For example
Input 8
Output true (2 is a prime divisor of 8, and 2x2=4 is also a divisor of 8.)

Input 50
Output true (5 is a prime divisor of 50, and 5x5=25 is also a divisor of 50.)

Write a program to check if the user input is a Lab number or not.
'''

#Dividers finding funcion
def dividers_founder(a):
    #without 1 cuz 1 is divider of everything
    repe = 2
    #list of dividers of given a
    dividers = []
    #adding dividers to list
    while repe <= a:
        if a % repe == 0:
            dividers.append(repe)
        repe = repe + 1
    return dividers
#Checking if number is prime
def prime_checker(b):
    x=2
    while x < b//2:
        if b%x == 0:
            return False
        else:
            x += 1
    return True
#Taking number from user
given_number = int(input("Podaj numer aby sprawdzić czy jest Lab Number\n"))
dividers_list = dividers_founder(given_number)
prime_dividers = []
#Creates list of prime dividers
for each_divider in dividers_list:
    if prime_checker(each_divider):
        prime_dividers.append(each_divider)
#Checking if number is Lab Number
lab_num = False
for each_prime_divider in prime_dividers:
    if each_prime_divider**2 in dividers_list:
        lab_num = True
        break

if lab_num:
    print("Twój numer jest Lab Number, ponieważ ma dzielnik który jest liczbą pierwszą i wynosi", each_prime_divider, "oraz podniesiony do potęgi 2 wynosi", each_prime_divider**2, "który również jest dzielnikiem twojej liczby")
else:
    print("Nie jest Lab Number, gdyż z dzielników pierwszych jakie posiada ta liczba, czyli", prime_dividers, "nie ma takiej która podniesiona do potęgi 2 również jest dzielnikiem tej liczbym, a zatem", dividers_list)
