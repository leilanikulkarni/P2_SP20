# More on loops
import random
# Basic FOR loop
for i in range(5, 51, 5):
    print(i, end=" ")  # use this for printing characters in hangman
print()

# RANGE function (alternative for comprehension)
my_list = [x for x in range(100)]
print(my_list)

my_list = range(100)  # iterable
print(my_list)

# BREAK (breaks out of the loop)
for number in my_list:
    if number > 10:
        break  # exits the loop entirely
    print(number, end=" ")

print("End of the loop")

# CONTINUE (skips to the end of the loop for that iteration (skips over numbers that multiples of 7 in this case)
for number in my_list:
    if number % 7 == 0:
        continue
    print(number, end=" ")


# FOR ELSE
for number in my_list:
    print(number, end=" ")
    if number == 80:
        break
else:
    print("The loop completed naturally")

# Add me as a collaborator on Github

my_list = ["A", "B", "C"]

my_word = my_list.pop(random.randrange(len(my_list)))
print(my_word, my_list)

random.shuffle(my_list)
used_letters = ["A", "S", "T"]
my_word = "GHOST"
for letter in my_word:
    if letter in used_letters:
        print(letter, end=" ")
    else:
        print("_", end=" ")
