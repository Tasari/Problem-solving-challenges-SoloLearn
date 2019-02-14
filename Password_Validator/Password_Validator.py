'''
Password Validator

Password validator is a program that validates passwords to match specific rules. For example, the minimum length of the password must be eight characters long and it should have at least one uppercase letter in it. 

A valid password is the one that conforms to the following rules:
 - Minimum length is 5;
 - Maximum length is 10;
 - Should contain at least one number;
 - Should contain at least one special character (such as &, +, @, $, #, %, etc.);
 - Should not contain spaces.

Examples:
Input: "Sololearn"
Output: false

Input: "John Doe"
Output: false

Input: "$ololearn7"
Output: true

Write a program to checks if the user input is a valid password or not.
'''

given_password = input("Podaj hasło jakie chcesz sprawdzić\n")
#assuming given pass is having good lenght and don't have space,
#but no special char and number
lenght = True
no_space = True
special_char = False
number = False
#checking lenght of password
if len(given_password) < 5:
    print('Hasło musi być dłuższe niż 5 znaków')
    lenght = False
elif len(given_password) > 10:
    print('Hasło musi być krótsze niż 10 znaków')
    lenght = False
#checking if there is space
for each_letter in given_password:
    if ord(each_letter) == 32:
        no_space = False
#checking if there is special char
    if ord(each_letter) > 32 and ord(each_letter) < 48:
        special_char = True
    elif ord(each_letter) > 57 and ord(each_letter) < 65:
        special_char = True
    elif ord(each_letter) > 90 and ord(each_letter) < 97:
        special_char = True
    elif ord(each_letter) > 122 and ord(each_letter) < 127:
        special_char = True
#checking if there is number
    if ord(each_letter)>48 and ord(each_letter)<57:
        number = True
#checking values of restrictions
if no_space and special_char and lenght and number:
    print('Hasło jest poprawne')
if no_space == False:
    print('Hasło nie może zawierać spacji')
if special_char == False:
    print('Hasło musi zawierać znak specjalny')
if number == False:
    print('Hasło musi zawierać cyfrę')
