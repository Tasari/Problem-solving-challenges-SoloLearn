# Problem solving challenges SoloLearn
Repository containing solved challenges from SoloLearn's mobile app
## Content:
1. [Totatives](#totatives)
2. [Anadrome](#anadrome)
3. [Array Partitioning](#array_partitioning)

### Totatives
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

### Anadrome

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

### Array_Partitioning
Divide a given array of numbers into two subarrays such that
the absolute difference between their sums is the smallest possible. 
For example, the array [2, 5, 4, 7, 15, 20] can be
divided into subarrays [15, 7, 4] and [20, 5, 2]. 
The difference between the sums of those arrays is 1, and it is the smallest.
For example:
Input:
6
4, 15, 20, 2, 7, 5
Output:
[15, 7, 4]
[20, 5, 2]
1
(The sum of the first subarray is 26, the sum of the second subarray is 27
, the difference is 1.)
The first line of the input contains the size of the array.
The next line contains the array elements. 
#Since giving an array might be a problem for user, i created array filler
Print the subarrays and the difference of their sums.

