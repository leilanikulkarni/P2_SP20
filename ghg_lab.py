
'''
Greenhouse gas emissions (GHG) vs. square footage for all school buildings in Chicago

Data set used will be Chicago Energy Benchmark info from 2018
data can be found at...
https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD

Energy Efficiency of Chicago Schools (35pts)

Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
The dataset at the link above is that data from 2015 to 2018.
We will use this data to look at schools.  We will visualize the efficiency of schools by scatter plot.
We expect that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
Challenge (for fun):
An efficient school would have a large ratio of sqft to ghg.
It would also be interesting to know where Parker lies on this graph???  Let's find out.

Make a scatterplot which does the following:
- Scatter plot the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (10pts)
- Data includes ONLY data for K-12 Schools. (5pts)
- Data includes ONLY data for 2018 reporting. (5pts)
- Label x and y axis and give appropriate title. (5pts)
- Annotate Francis W. Parker. (5pts) (annotated Latin because Francis W. Parker only has data from 2016)
- Create a best fit line for schools shown. (5pts)

Extra Credit: Add a significant feature to your graph that helps tell the story of your data.  (feel free to use methods from matplotlib.org). (10pts)

Note: With extra credit you will earn you a max of 35pts (100%) for the assignment.
Maybe you can try one of the following or think up your own:
- Annotated labels (school name) for the 3 highest and 3 lowest GHG Intensities.
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)


Note 2:  This is a tough assignment to do on your own.  Do your best with what you have.
'''

import csv
import requests
import matplotlib.pyplot as plt
import numpy as np  # importing the libraries I will need

def get_data(url):
    with requests.Session() as s:
        download = s.get(url)
        content = download.content.decode('utf-8')
        reader = csv.reader(content.splitlines(), delimiter=',')
        my_list = list(reader)
    return my_list  # getting the csv and list that we will need


data = get_data("https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD")  # importing the data
header = data.pop(0)

print(header)  # popping off and printing the headers

ghg_index = header.index("Total GHG Emissions (Metric Tons CO2e)")
sq_ft_index = header.index("Gross Floor Area - Buildings (sq ft)")
type_index = header.index("Primary Property Type")
year_index = header.index("Data Year")
ghg_intensity_index = header.index("GHG Intensity (kg CO2e/sq ft)")  # creating indexes for all the information I will need


valid_k_12_data = []
valid_data = []
print(len(data))

school_list = []  # creating empty lists to put the sorted data in

for building in data:
    try:
        int(building[ghg_index])
        int(building[sq_ft_index])  # converting this information into integers
        if building[type_index] == "K-12 School":
            valid_k_12_data.append(building)
    except:
        pass  # checking to see if the building is a K-12 school

for building in valid_k_12_data:
    try:
        int(building[ghg_index])
        int(building[sq_ft_index])  # converting this information into integers
        if building[year_index] == "2018":
            valid_data.append(building)
    except:
        pass  # checking to see if the data was logged in 2018

print(len(valid_data))

ghg = [int(x[ghg_index]) for x in valid_data]
sq_ft = [float(x[sq_ft_index]) for x in valid_data]
ghg_intensity = [float(x[ghg_intensity_index]) for x in valid_data]  # creating the variables that I will use to graph

color = []
ghg_intensity_list = []
for building in ghg_intensity:
    ghg_intensity_list.append(building)  # creating a list for the GHG intensity

for building in ghg_intensity_list:
    if building > 10:
        color.append("green")
    else:
        color.append("red")  # if it is in the top 10% of GHG intensities, its color will be green on the graph;
        # otherwise, it will be shown in red


plt.figure(1, tight_layout=True)
plt.ylabel("Total Greenhouse Gas (GHG) Emissions")
plt.xlabel("Building Square Footage")
plt.title("GHG Emissions vs. K-12 School Square Footage")
plt.scatter(sq_ft, ghg, alpha=0.3, c=color)  # creating the axes and labelling the graph

for item in valid_data:
    school_list.append(item[2])

for i in range(len(school_list)):
    if school_list[i] == "Latin School of Chicago Upper School":
        plt.annotate("Latin School of Chicago Upper School", xy=(sq_ft[i], ghg[i]))  # annotating Latin Upper School
        # because FWP's data is from 2016 and not 2018

p = np.polyfit(sq_ft, ghg, 1)
print(p)

x = [x for x in range(500000)]
y = [p[0] * y + p[1] for y in x]


plt.plot(x, y)  # creating and plotting the best fit line

plt.show()  # showing the graph

