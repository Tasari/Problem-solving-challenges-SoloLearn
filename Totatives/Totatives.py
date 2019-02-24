'''Totatives
In number theory, Euler's totient function (phi function),
counts the positive integers up to a given integer n that are relatively prime to n.
Two integers are said to be relatively prime,
if the only positive integer (factor) that divides both of them is 1.

The numbers less than or equal to and relatively prime to a given number n are called totatives.


For example:
Input: 9
Output: 6
(The totatives of n = 9 are six numbers 1, 2, 4, 5, 7 and 8, so phi(9) = 6 because 3, 6 and 9 are not relatively prime with 9)


Note that, phi(1)=1 because 1 is considered to be relatively prime to every positive number.
Write a program to take positive integer n as an input and print the number of totatives in the numbers less than or equal to n.
'''


#Dividers finding funcion
def dividers(a):
    #without 1 cuz 1 is always divider and is always relatively prime
    repe = 2
    #list of dividers of given a
    dividers = []
    #adding dividers to list
    while repe <= a:
        if a % repe == 0:
            dividers.append(repe)
        repe = repe + 1
    return dividers


def phi(b):
    #creating list of all numbers up to b
    relprim = list(range(1,b)) 
    result_nubers = list(range(1,b))
    #creating list of dividers of b (In order to speed up the process a little)
    divib = dividers(b)
    #itering through every number up to b
    print(relprim, 'posiada dzielniki', divib)
    for rel in relprim:
        print('Liczba', rel)
        #iterating through all dividers of actual number
        for div in dividers(rel):
            print(div)
            #checking if any divider is in dividers of b
            if div in divib and rel in result_nubers:
                #if yes, then removes the number from list of all numbers up to b
                print("Usuwanie liczby",rel, "gdyż posiada dzielnik", div, "obecny w dzielnikach numeru", b)
                result_nubers.remove(rel)

    print(result_nubers)
    x = len(result_nubers)
    return x

#Infinite loop taking input from user
while 1:
    choice = int(input("Podaj dodatnią liczbę, najlepiej mniejszą niż 1000 bo inaczej chwilę to zajmie\n"))
    if  choice < 0:
        print("Dodatnią mate")
        continue
    elif choice > 2000:
        if input('Jeśli na pewno chcesz podać liczbę większą od 2000 wpisz "TAK"\n') == 'TAK':
            print("Totative numeru który wybrałeś wynosi", phi(choice))
            break
        else:
            continue
    else:
        print("Totative numeru który wybrałeś wynosi", phi(choice))
        break