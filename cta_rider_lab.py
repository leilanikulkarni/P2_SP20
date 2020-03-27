import csv
import matplotlib.pyplot as plt

'''
CTA Ridership (25pts)

Get the csv from the following data set.
https://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv?accessType=DOWNLOAD
This shows CTA ridership by year going back to the 80s
It has been updated with 2018 data, but not yet with 2019 unfortunately


1  Make a line plot of rail usage for the last 10 years of data.  (year on x axis, and ridership on y) (5pts)
2  Plot bus usage for the same years as a second line on your graph. (5pts)
3  Plot total usage on a third line on your graph. (5pts)
4  Add a title and label your axes. (4pts)
5  Add a legend to show data represented by each of the three lines. (4pts)
6  What trend or trends do you see in the data?  Offer a hypotheses which might explain the trend(s). Just add a 
comment here to explain. (2pts)


Hypotheses on CTA Ridership in the Last Ten Years:
First, some trends I see in the data are that both the bus and total usage have gone down, while rail usage has gone up.
For the reason the total usage went down the past ten years, I think that is because the bus usage affected that total.
Here is my hypothesis for why train (rail) usage has gone up and bus usage has gone down. I think the train usage 
started off fairly low because of the cost; it takes more money to build a train than it does a bus. However, with 
advancing technology, trains have gotten cheaper, so therefore, more people use them because the cost is less. 
Additionally, less people are owning cars in the past 10 years, so that can also contribute to more train 
usage. On the other hand, more people used to take the bus because the cost was much lower, but, after possibly trying 
to keep the buses cleaner, the cost went up, and less people decided to use the bus.
'''

with open("cta_ridership_boarding_totals.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

headers = data.pop(0)
print(headers)

years = [int(x[0]) for x in data]
last_ten_years = years[-10:]

names = [int(x[3]) for x in data]
last_ten_names = names[-10:]

buses = [int(x[1]) for x in data]
last_ten_buses = buses[-10:]

total = [int(x[4]) for x in data]
last_ten_years_total = total[-10:]


plt.title("CTA Ridership in the Last Ten Years", fontsize=20, color="blue")
plt.ylabel("Ridership")
plt.xlabel("Years")


plt.plot(last_ten_years, last_ten_names, label="Rail Usage")
plt.plot(last_ten_years, last_ten_buses, label="Bus Usage")
plt.plot(last_ten_years, last_ten_years_total, label="Total Usage")

plt.legend(fancybox=True, shadow=True)
plt.show()
