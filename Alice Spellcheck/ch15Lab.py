'''
Complete the chapter lab at https://docs.google.com/document/d/1KjrNiE3mUbaeyTPpaTesAlnVYkp0KkkM-17oOKqscjw/edit?usp=sharing
'''

# Successful linear spellcheck (10pts)
# Successful binary spellcheck (10pts)
# Binary and linear are written as functions (5pts)

import re


def split_line(line):
    # This function takes in a line of text and returns
    # a list of words in the line.
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


with open('dictionary.txt') as f:
    dictionary_list = [x.strip().upper() for x in f]

f.close()

print("--- Linear Search ---")

alice_in_wonderland_200 = open('AliceInWonderland200.txt')


def linear_search():
    line_number = 0
    for line in alice_in_wonderland_200:
        line_number += 1
        words = split_line(line)
        for word in words:
            i = 0
            word_found = False
            while i < (len(dictionary_list)) and word.upper() != dictionary_list[i]:
                i += 1

            if i < len(dictionary_list) - 1:
                word_found = True

            else:
                print(line_number, word.upper())


linear_search()

print("--- Binary Search ---")


def binary_search():
    line_number = 0
    for line in alice_in_wonderland_200:
        line_number += 1
        words = split_line(line)
        for word in words:
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False
            while lower_bound <= upper_bound and not found:
                middle_pos = (upper_bound + lower_bound) // 2
                if dictionary_list[middle_pos] < word.upper():
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > word.upper():
                    upper_bound = middle_pos - 1
                else:
                    found = True
            if not found:
                print(line_number, word.upper())


binary_search()


# Challenge:  Find all words that occur in Alice through the looking glass that do NOT occur in Wonderland.


# with open('AliceInWonderland.txt') as f:
#     alice_in_wonderland = [x.strip().upper() for x in f]
#
# f.close()
#
# print("--- Challenge Problem ---")
#
# alice_through_looking_glass = open('AliceThroughTheLookingGlass.txt')
#
# alice_in_wonderland.sort()


# def alice_in_looking_glass():
#     line_number = 0
#     for line in alice_through_looking_glass:
#         line_number += 1
#         words = split_line(line)
#         for word in words:
#             i = 0
#             word_found = False
#             while i < (len(alice_in_wonderland)) and word.upper() != alice_in_wonderland[i]:
#                 i += 1
#
#             if i < len(alice_in_wonderland) - 1:
#                 word_found = True
#
#             else:
#                 print(line_number, word.upper())
#
#
# alice_in_looking_glass()

# prints every letter in alice through the looking glass so i commented it out

