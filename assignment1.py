# #even number from m to n
# m = input("Enter the first number")
# n = input("Enter the second number")
#
# for num in range(m, n):
#     if num%2 == 0:
#         print num

################# PERFECT NUMBER ####################

# # print all perfect number from 0 to n
#
# #perfect number function
# def perfectNumber(m):
#     # logic to check for perfect number
#     sum = 0;
#     for num in range(1, m):
#         if m % num == 0:
#             sum = sum + num
#
#     if sum == m:
#         print "Perfect Number is", m
#
# n = input("Enter the number")
#
# #checeking perfect numbers for n numbers
# for i in range(1, n):
#     perfectNumber(i)

######################### PRIME NUMBER ########################

#print prime numbers from m to n

# x = input("Enter start number")
# y = input("Enter last number")
#
# #function for prime number
# def primeNumber(m):
#     isPrime = False
#     for i in range(2, (m/2+1)):
#         if m%i == 0:
#             isPrime = False
#         else:
#             isPrime = True
#     #checking the isPrime variabele
#     if isPrime:
#         print m
#
# #checking prime numbers between x and y
# for num in range(x, y):
#     primeNumber(num)

######################### FABONACCI SERIES ########################

# num = input("Enter a number for the length of Fabonacci Series")
# #function for fabonacci series
# def fabonacci(n):
#     previous = 0
#     current = 1
#     total = 0
#
#     for i in range(0, n):
#         print total
#         #print current
#         total = previous + current
#         previous = current
#         current = total
# fabonacci(num)

######################### MERGE AND PRINT ARRAY INTERSECTION ########################

# #creating three empty lists/arrays
# array1 = []
# array2 = []
# array3 = []
#
# #getting the sizes of the arrays
# x = input("Enter the length of first array")
# y = input("Enter the length of second array")
#
# #filling the first array through user
# for i in range(0, x):
#     temp = input("Enter element to fill the array1")
#     array1.append(temp)
#
# #filling the second array through user
# for i in range(0, y):
#     temp = input("Enter element to fill the array2")
#     array2.append(temp)
#
# #checking for intersection and storing in a new array
# for i in range(0, x):
#     for j in range(0, y):
#         if array1[i] == array2[j]:
#             array3.append(array1[i])
#
# #printing all the arrays
# print array1, array2, array3

######################### GIVEN AN ARRAY A GENERATE ARRAY Y WHERE Y=2*A+1 ########################

# #creating two empty lists/arrays
# array1 = []
# #array2 = []
#
# #getting the sizes of the arrays
# x = input("Enter the length of first array")
#
# #filling the first array through user
# for i in range(0, x):
#     temp = input("Enter element to fill the array1")
#     array1.append(temp)
#
# #creating second array 2*array1+1
# array2 = [(i*2+1) for i in array1]
#
# print array1, array2

######################### REVERSE A STRING ########################

# word = raw_input("Enter the string you want to reverse")
#
# #get the entered string in an array
# array1 = [i for i in word]
#
# # #reversing the array
# # for i in range(0, len(reverse)):
# #     last = len(reverse)-1
# #     temp = reverse[last-i]
# #     reverse[last-i] = reverse[i]
# #     print reverse[last-i]
# #     reverse[i] = temp
#
# reverse = []
# for i in range((len(array1)-1), -1, -1):
#     reverse.append(array1[i])
#
# #printing the array
# print reverse

######################### CHECK PALANDROME ########################

# word = raw_input("Please enter the word")
# isPalandrome = False
#
# array = [i for i in word]
#
# print array
#
# for i in range(0, len(array)):
#     last = len(array)-1
#     if array[i] == array[last-i]:
#         isPalandrome = True
#     else:
#         isPalandrome = False
#
# if isPalandrome:
#     print "The word is palandrome"
# else:
#     print "The word is not palandrome"

######################### CHECK ANAGRAM ########################

word1 = raw_input("Enter the first word")
word2 = raw_input("Enter the second word")
array1 = [i for i in word1]
array2 = [i for i in word2]

if len(array1) == len(array2):
    for i in array1:
        for j in array2:
            if i == j:
                isAnagram = True
                array2.remove(j)
                break
            else:
                isAnagram = False
    if isAnagram:
        print "Is an Anagram"
    else:
        print "Not an Anagram"
else:
    print "Not an Anagram"
