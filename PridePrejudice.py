'''
Pride and Prejudice (25pts)

This lab is largely review of: lists, comprehensions, requests, string methods, matplotlib.
The only new item here is using a dictionary (dict).

We will use list, dictionary, and graphing skills to do a basic analysis of Jane Austen's Pride and Prejudice.
Your task is to create a bar graph of the 25 most common words.


A common Python pattern to count objects, produce histograms, or update stats is to make calls to a dictionary
as you iterate through a list. For example, given a list of words, you can create a dictionary to store counts and then
iterate through the list of words, checking how many times each word has appeared using your dictionary, and updating
the dictionary count now that you've seen that word again.
'''


# PSEUDO CODE
# Get text from http://www.gutenberg.org/files/1342/1342-0.txt - Use requests library.
# Split the transcript into words - Use split and strip methods and store results in a list.
# Create a dictionary object to store the word counts
# Iterate through the list/text of Pride and Prejudice
# Update word counts on your dict (10pts)
# Sort words by counts in descending order (5pts)
# Create Bar Graph (5pts)
# Include descriptive titles and labels (5pts)

import requests
import matplotlib.pyplot as plt

url = "http://www.gutenberg.org/files/1342/1342-0.txt"
pride_prejudice = requests.get(url).text  # getting the url

print(pride_prejudice[:1000])

word_list = pride_prejudice.split()
word_list = [x.upper().strip(' ?.:;!\\<>{}\n\t') for x in word_list]

print(word_list[:1000])

pp_dictionary = {}  # creating an empty dictionary

for word in word_list:
    if word in pp_dictionary:
        pp_dictionary[word] += 1
    else:
        pp_dictionary = 1  # adding the words to pp_dictionary

sorted_pp_dictionary = sorted(pp_dictionary)
sorted_pp_dictionary.reverse()  # putting pp_dictionary in reverse/descending order

top_25_dict = {}  # creating the top 25 empty dictionary

for i in range(25):
    if pp_dictionary[i] in top_25_dict:
        top_25_dict[i] += 1
    else:
        top_25_dict = 1  # adding pp_dictionary words to the top 25 dictionary

plt.bar(top_25_dict.keys(), top_25_dict.values())  # plotting the keys on the x-axis and the values on the y-axis
plt.xlabel("Words in Pride and Prejudice")  # creating an x-axis label
plt.ylabel("How many times that word occurs")  # creating a y-axis label
plt.title("How many times each word in Pride and Prejudice occurs")  # creating a title

plt.show()  # showing the bar graph


# CHALLENGE (OPTIONAL)
# Here is a list of the 1000 most common words in English:
# https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt
# Make your plot show the 25 most common words in Hamlet NOT in this list.

# MORE CHALLENGES
# look at Project Gutenberg, and try another book and see if your algorithms hold up.
# HERE IS A LIST OF NEGATIVE WORDS.  Evaluate a text for percentage of negative words.
# Try the same for positive.  Or do both to evaluate the mood of a book.  Compare Mark Twain to Edgar Allan Poe.
# https://gist.githubusercontent.com/mkulakowski2/4289441/raw/dad8b64b307cd6df8068a379079becbb3f91101a/negative-words.
# txt