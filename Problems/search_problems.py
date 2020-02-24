'''
Searching problems (25pts)
Complete the following 3 searching problems using techniques
from class and from the notes and the textbook website.
Solutions should use code to find and print the answer.
'''
import re

with open('AliceInWonderLand.txt', 'r') as file:
    alice_in_wonderland = [x.strip().upper() for x in file]


def split_line(line):
    # uses regular expressions to split line of text into word list
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# 1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.
len_word = 0
longest_word = " "

with open('dictionary.txt', 'r') as file:
    dictionary_list = [x.strip().upper() for x in file]
    for word in dictionary_list:
        if len(word) > len_word:
            longest_word = word
            len_word = len(word)

print(longest_word)

# 2.  (8pts)  Write code which finds the total word count AND average word length
# in "AliceInWonderLand.txt"

amount_of_words_in_alice = []

for line in alice_in_wonderland:
    words = split_line(line)

    for word in words:
        amount_of_words_in_alice.append(word)

print(len(amount_of_words_in_alice))

word_list = []
sum_alice_words = 0

for line in alice_in_wonderland:
    words = split_line(line)
    for word in words:
        word_list.append(word)
        sum_alice_words += len(word)
avg_alice_words = sum_alice_words / len(word_list)
print(avg_alice_words)

# 3.  (3pts)  How many times does the name Alice appear in Alice in Wonderland?

alice = 0
for line in alice_in_wonderland:
    words = split_line(line)

    for word in words:
        if word == "Alice".upper():
            alice += 1

print(alice)


# 4.  (6pts) Find the most frequently occurring seven letter word in "AliceInWonderLand.txt"
seven_letter_words = []
for line in alice_in_wonderland:
    words = split_line(line)

    for word in words:
        if len(word) == 7:
            seven_letter_words.append(word)

seven_letter_word = seven_letter_words[0]
first_instance = 0

for word in seven_letter_words:
    word_instances = seven_letter_words.count(word)
    if word_instances > first_instance:
        seven_letter_word = word
        first_instance = word_instances

print(seven_letter_word)

# 5.  (2pts, small points challenge problem)
# How many times does "Cheshire" occur in"AliceInWonderLand.txt"?

cheshire = 0
for line in alice_in_wonderland:
    words = split_line(line)

    for word in words:
        if word == "Cheshire".upper():
            cheshire += 1

print(cheshire)

# How many times does "Cat" occur?

cat = 0
for line in alice_in_wonderland:
    words = split_line(line)

    for word in words:
        if word == "Cat".upper():
            cat += 1

print(cat)

# How many times does "Cheshire" immediately followed by "Cat" occur?
cheshire_cat = 0

key = "Cheshire".upper()
for line in alice_in_wonderland:
    words = split_line(line)
    i = 0
    while i < (len(words) - 1) and key != words[i]:
        i += 1

    if i < len(words) - 1:
        if words[i + 1] == "Cat".upper():
            cheshire_cat += 1

print(cheshire_cat)
