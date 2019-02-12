'''
Anadrome

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
For example, "Sool" is an anagram for "Solo".
A palindrome is a word or phrase which reads the same backward as forward, such as "madam".
An anadrome is a word or phrase if any of its anagrams form a palindrome.

For example:
Input: "SoloSolo"
Output: yes ("SoollooS" is an anagram of "SoloSolo" which also is a palindrome).

Input: "3haha"
Output: yes ("ha3ah" is an anagram of "3haha" which also is a palindrome).

Input: "Solo"
Output: no

Write a program to check if the user input is an anadrome or not
'''
import re

#function which counts letters in word and gives back list where index means number ascii of letter
def asciicode_letters(word):
    asciicode = 0
    letters = [0]*128
    while asciicode <129:
        for a in word:#compare each letter in word to every letter in ascii
            if a == chr(asciicode):#if matches, increase amount in list under the given index
                letters[asciicode] += 1
        asciicode += 1
    return letters



given_word_normal = input("Podaj słowo, które ma być sprawdzone:\n")
given_word = given_word_normal.lower() #ignoring upper and lower case
lenght = len(given_word)
if lenght % 2 != 0:
    chance = True #if word has odd number of letters then give possibility to have letter without pair
else:
    chance = False
letters = asciicode_letters(given_word)
for any_letter in letters:#any letter in ascii code
    if any_letter % 2 != 0:
        if chance == True:#if there is possibility of lone letter use it
            chance = False
        else:
            print('Wyraz "{}" nie jest anadromem'.format(given_word_normal))
            exit(0)
print('Wyraz "{}" jest anadromem'.format(given_word_normal))



        
    

