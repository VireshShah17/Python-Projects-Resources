""" R.1) Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise."""


# def multiple(n, m):
#   if n % m == 0:
#     return f"True!{n} is multiple of {m}"
#   else:
#     return f"False!{n} is not a multiple of {m}"
#
#
# print(multiple(16, 3))

''' R.2) Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.'''


# def is_even(k):
#   if (-1) ** k == 1:
#     print(f"{k} is an even number")
#   else:
#     print(f"{k} is an odd number")
#
#
# is_even(8)

""" R.3) Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution."""


# def minmax(data):
#   biggest = smallest = data[0]
#   try:
#     for num in data:
#       if num >= biggest:
#         biggest = num
#       if num <= smallest:
#         smallest = num
#     print(f"The largest number is {biggest}")
#     print(f"The smallest number is {smallest}")
#   except Exception as excpt:
#     print("Bad input found", excpt)
#
#
# num_list = [10, 14, 48, 5, 16]
# minmax(num_list)

""" R.4) Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n."""


# def sqr_sum(num):
#     sums = 0
#     i = 0
#     while i <= num:
#         sums += i ** 2
#         i += 1
#     print(f"The sum of integers is: {sums}")
#
#
# sqr_sum(5)

"""R.5) Give a single command that computes the sum from Exercise R-1.4, 
relying on Python’s comprehension syntax and the built-in sum function"""


# def sqr_sum(num):
#     return sum([k**2 for k in range(num + 1)])
#
#
# print(f"The sum of integers is: {sqr_sum(5)}")

"""R.6) Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n."""


# def odd_sqr_sum(num):
#     odd_sum = 0
#     for i in range(num + 1):
#         if i % 2 == 0:
#             continue
#         else:
#             odd_sum += i ** 2
#     print(f"The sum of odd square integers is {odd_sum}")
#
#
# odd_sqr_sum(5)

"""R.7) Give a single command that computes the sum from Exercise R-1.6, 
relying on Python’s comprehension syntax and the built-in sum function"""


# def odd_sqr_sum(num):
#     return sum([k ** 2 for k in range(1,num + 1, 2)])
#
#
# print(f"The sum of odd square integers is {odd_sqr_sum(5)}")

"""C.1) Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing."""


# def rev_list(lst):
#     new_lst = []
#     for i in range(len(lst) - 1, -1, -1):
#         new_lst.append(lst[i])
#     return new_lst
#
#
# print(f"The reversed list is {rev_list([1, 2, 3, 4, 5])}")

"""C.2) Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd"""


# def odd_product(nums):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i != j:
#                 product = nums[i] * nums[j]
#                 if product & 1:
#                     return True
#     return False
#
#
# dt1 = [2, 4, 6, 8]
# print(odd_product(dt1))

"""C.3) Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct)."""


# def distinct_nums(nums):
#     checker = False
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i != j:
#                 if nums[i] == nums[j]:
#                     checker = False
#                     break
#                 else:
#                     checker = True
#     return checker
#
#
# print(f"Are there distinct numbers in list: {distinct_nums([2, 4, 6, 8])}")

"""C.4) Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n−1."""


# def dot_product(a,  b):
#     c = []
#     for i in range(0, len(a)):
#         c.append(a[i] * b[i])
#     return c
#
#
# first = [1, 2, 3, 4]
# second = [1, 2, 3, 4]
# print(dot_product(first, second))

"""C.5) Write a short Python function that counts the number of vowels in a given
character string"""


# def count_vowel(given_str):
#     vowel_count = 0
#     for ch in given_str:
#         if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
#             vowel_count += 1
#     return vowel_count
#
#
# random_str = "My name is Viresh!"
# print(count_vowel(random_str))

"""P.1) Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2."""


def num_less_2(num):
    count = 0
    while num >= 2:
        num /= 2
        count +=1
    return count


print(f"It should be divided {num_less_2(10)} times by 2")
