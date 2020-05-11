'''
Sorting and Intro to Big Data Problems (22pts)
Import the data from NBAStats.py.  The data is all in a single list called 'data'.
I pulled this data from the csv in the same folder and converted it into a list for you already.
For all answers, show your work
Use combinations of sorting, list comprehensions, filtering or other techniques to get the answers.
'''
from NBAStats import *
# 1  Pop off the first item in the list and print it.  It contains the column headers. (1pt)
column_headers = data.pop(0)
print(column_headers)

# 2  Print the names of the top ten highest scoring single seasons in NBA history?
# You should use the PTS (points) column to sort the data. (4pts)
data.sort(key=lambda x: x[-1])
for player in range(len(data) - 11, len(data)):
    print(data[player][2])

# 3  How many career points did Kobe Bryant have? Add up all of his seasons. (4pts)
print(int(sum([x[-1] for x in data if x[2] == "Kobe Bryant"])))

# 4  What player has the most 3point field goals in a single season. (3pts)

data.sort(key=lambda x: x[-19])
print(data[-1][2])

# 5  One stat featured in this data set is Win Shares(WS).
#  WS attempts to divvy up credit for team success to the individuals on the team.
#  WS/48 is also in this data.  It measures win shares per 48 minutes (WS per game).
#  Who has the highest WS/48 season of all time? (4pts)

ws_48_list = sorted(data, key=lambda x: x[25])
print(ws_48_list[-1][2])

# 6  Write your own question that you have about the data and provide an answer (4pts)
# Maybe something like: "Who is the oldest player of all time?"  or "Who played the most games?"  or "Who has the most
# combined blocks and steals?".

question = "Who is the oldest player in the NBA?"
age = column_headers.index("Age")
data.sort(key=lambda x: x[age])
print(data[-1][2])

# 7  Big challenge, few points.  Of the 100 highest scoring single seasons in NBA history, which player has the
# worst free throw percentage?  Which had the best? (2pts)

data.sort(key=lambda x: x[-1])

data.sort(key=lambda x: x[-10])

print("Worst:", data[-99][2])
print("Best:", data[-1][2])
