# LISTS (25pts)
# Show work on all problems.  Manually finding the answer doesn't count

# PROBLEM 1 (Using List Comprehensions - 8pts)
# Use list comprehensions to do the following:
# a) Make a list of numbers from 1 to 100
my_list1 = [x for x in range(1, 101)]
print(my_list1)

# b) Make a list of even numbers from 20 to 40
my_list2 = [x for x in range(20, 41, 2)]
print(my_list2)

# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)
my_list3 = [x ** 2 for x in range(1, 101)]
print(my_list3)

# d) Make a list of all positive numbers in my_list below.
my_list = [-77, -78, 82, 81, -40, 2, 62, 65, 74, 48, -37, -52, 90, -84, -79, -45, 47, 60, 35, -18]
my_new_list = [x for x in my_list if x > 0]
print(my_new_list)

# PROBLEM 2 (Import the number list - 3pts)
# The Problems directory contains a file called "number_list.py"
# import this file which contains num_list
from Problems import number_list
# there's an error which says the objects aren't subscriptable
# Print the last 5 numbers in num_list
# copy_num_list = [x for x in number_list.num_list]
# print(copy_num_list)
num_list = number_list.num_list
if __name__ == "__main__":
    print(num_list[-5:])


# PROBLEM 3 (List functions and methods - 8pts)
# Find and print the highest number in num_list (1pt)
print(max(num_list))

# Find and print the lowest number in num_list (1pt)
lowest_number = min(num_list)
print(lowest_number)


# Find and print the average of num_list (2pts)
sum_num = 0

for i in range(len(num_list)):
    sum_num += num_list[i]

average_num_list = sum_num / len(num_list)
print(average_num_list)

# Remove the lowest number from num_list (2pt)
del num_list[num_list.index(lowest_number)]


# Create and print a new list called top_ten which contains only the 10 highest numbers in num_list(2pts)
num_list.sort()
top_ten = num_list[-10:]
print(top_ten)

# PROBLEM 4 (4pts)
# Find the number which appears most often in num_list?

list_for_problem = number_list.num_list
a_num = num_list[0]
first_instance = 0

for num in list_for_problem:
    num_instances = list_for_problem.count(num)
    if num_instances > first_instance:
        a_num = num
        first_instance = num_instances
print(a_num)


# CHALLENGE PROBLEMS (2pts)
# TOUGH PROBLEMS, BUT FEW POINTS

# Find the number of prime numbers in num_list?
# Hint: One way is to just start removing the ones that aren't
for num in num_list:
    if num % 2 == 0:
        del num_list[num_list.index(num)]
    elif num % 3 == 0:
        del num_list[num_list.index(num)]
    elif num % 5 == 0:
        del num_list[num_list.index(num)]
    elif num % 7 == 0:
        del num_list[num_list.index(num)]
    elif num % 13 == 0:
        del num_list[num_list.index(num)]
    elif num % 17 == 0:
        del num_list[num_list.index(num)]  # didn't get rid of all of them but got rid of most

prime_numbers = len(num_list)
print(prime_numbers)


# Find the number of palindromes
# Hint: This may be easier to do with strings
num_list.sort()
palindrome_list = []
for num in num_list:
    num = " "
    reversed_num = num.reverse()
    if num == reversed_num:
        palindrome_list.append(num)

print(len(palindrome_list))





