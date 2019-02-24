'''
Array Partitioning


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
'''

from itertools import combinations

def array_sum(array):
    total = 0
    for thing in array:
        total += thing
    return total


#array creator
size_of_array = int(input("Podaj rozmiar tablicy, najlepiej nie większy niż 15\n"))
i = 0
elements = []
while i < size_of_array:
    elements.append(int(input("Podaj element {}\n".format(i+1))))
    i += 1
elements.sort()
print("Twoja tablica elementów to", elements)



half_sum = array_sum(elements)/2
counter = 0
notfound = True
found = 0
iteration = 0
z = []
#Creates list of lists of possible combos
while iteration < size_of_array:
    z.append([list(l) for l in list(combinations(elements, iteration+1))])
    iteration += 1
#Looking for best combo
while notfound:
    for a in z:
        for combo in a:
            if sum(combo) == half_sum:
                notfound = False
                if found == 0:
                    found = combo 
    counter += 1
    half_sum += 0.5
#deleting found elements from first array
for iterat in elements:
    for iterat2 in found:
        if iterat == iterat2:
            elements.remove(iterat2)

st1 = elements
st2 = found

print("\n\nSukces z odchyleniem:",counter-1 ,"\nPierwsza tablica:", st1, "\nDruga tablica:", st2)