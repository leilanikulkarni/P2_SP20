# Folium train map


# 15pts - Use folium to plot all of the L train stops in Chicago. Use an appropriate start zoom level.
# 5pts - Add the name to each stop as a popup. Add a train icon to each marker.  Save as an html page in the same folder.
# 3pts  - Color code all of the lines (make the pink line marker pink etc.)
# 2pts - Brown is not a default color name.  See if you can use the documentation for Folium to set a marker color through other means.

# Data set is in this folder, but can be found at: https://data.cityofchicago.org/api/views/8pix-ypme/rows.csv?accessType=DOWNLOAD

# Tricky parts of this one
## The location is in tuple format.  If you have trouble converting it, try this:
my_string = '(41.2, -87.9)'
my_tuple = eval(my_string)
print(my_tuple)
print(type(my_tuple))

import csv
import folium

with open('CTA_-_System_Information_-_List_of__L__Stops (1).csv') as f:
    reader = csv.reader(f)
    data = list(reader)  # converted the csv file

cta_map = folium.Map(location=[41.8781, -87.6298], zoom_start=11) # create the baseline for the folium map

print(data.pop(0))  # print the headers
lat_longs = [eval(x[-1]) for x in data]  # find the latitude and longitude of each coordinate
popups = [x[2] for x in data]  # find the names of each train station

colors = []  # make a colors list
for stop in data:
    if stop[7]:
        colors.append('red')
    if stop[8]:
        colors.append('blue')
    if stop[9]:
        colors.append('green')
    if stop[10]:
        colors.append('beige')
    if stop[11]:
        colors.append('purple')
    if stop[11] or stop[12]:
        colors.append('lightgrey')
    if stop[13]:
        colors.append('white')
    if stop[14]:
        colors.append('pink')
    if stop[15]:
        colors.append('orange')
    else:
        colors.append('black')  # if the stop color is true, color becomes that, but if all are false, color is black

print(colors) # print colors

for i in range(len(lat_longs)):
    folium.Marker(location=lat_longs[i],
                  popup='<b>' + popups[i] + '</b>',
                  icon=(folium.Icon(prefix='fa', icon='train', color=colors[i]))).add_to(cta_map)  # print each stop with
    # the icon, color, and name, then add to the cta map

cta_map.save('train-map.html')

# If you have extra time, try to put some html into the popup.
