# SCRAPING PROBLEMS
# Twitter Scraping (15pts)
# Go to your favorite follow on Twitter.  (not someone who posts explicit materials please)
# Inspect the twitter feed in Chrome.
# You'll notice that the tweets are stored in a ordered list <ol></ol>, and individual tweets are contained as list items <li></li>.
# Use BeautifulSoup and requests to grab the text contents of last 5 tweetslocated on the twitter page you chose.
# Print the tweets in a nicely formatted way.
# Have fun.  Again, nothing explicit.

#  print("{} {}!".format("Hello", "World"))

# did not do this part because of Twitter complications

# Weather Scraping (15pts)
# Below is a link to a 10-day weather forecast at weather.com
# Pick the weather for a city that has the first letter as your name.
# Use requests and BeautifulSoup to scrape data from the weather table.
# Print a synopsis of the weather for the next 10 days.
# Include the day and date, description, high and low temp, chance of rain, and wind. (2pts each)
# Print the weather for each of the next 10 days to the user in a readable sentences.
# You can customize the text as you like, but it should be readable as a sentence without errors. (5pts)
# You will need to target specific classes or other attributes to pull some parts of the data.
# Sample sentence:
# Wednesday, April 4 will be Partly Cloudy/Windy with a High of 37 degrees and a low of 25, humidity at 52%.  There is 0% chance of rain with winds out of the WNW at 22 mph.
# if the sentence is a little different than shown, that will work; do what you can.  Don't forget about our friend string.format()

from bs4 import BeautifulSoup
import requests

url = "https://weather.com/weather/tenday/l/11ebc9e1c090378d16b0d092fddb4f43f1335de91c5660fe49893a323badbea4"

page = requests.get(url)  # requesting from url

soup = BeautifulSoup(page.text, "html.parser")  # complete list of data
soup.prettify()  # make the data look nicer

days = soup.find_all("span", class_="date-time")
day_list = [x.text for x in days]  # find days + convert into a list

dates = soup.find_all("span", class_="day-detail clearfix")
date_list = [x.text for x in dates]  # find dates + convert into a list

descriptions = soup.find_all("td", class_="description")
description_list = [x.text for x in descriptions]  # find descriptions + convert into a list

high_low_temps = soup.find_all("td", class_="temp")
high_low_temp_list = [x.text.replace("°", "°/ ", 1) for x in high_low_temps]  # find high + low temperatures + convert
# into a list

chances_of_rain = soup.find_all("td", class_="precip")
chance_of_rain_list = [x.text for x in chances_of_rain]  # find chances of rain + convert into a list

winds = soup.find_all("td", class_="wind")
wind_list = [x.text for x in winds]  # find wind direction and speed + convert into a list

humidity = soup.find_all("td", class_="humidity")
humidity_list = [x.text for x in humidity]  # find humidity percentage + convert into a list

print()
print("Luxembourg City, Luxembourg, 10 Day Forecast")
print("--------------------")
print()  # header for 10 day forecast

for i in range(10):
    print(day_list[i] + ", " + date_list[i].lower(), "will be", description_list[i].lower(), "with a high and low of",
          high_low_temp_list[i] + ", with the humidity at", humidity_list[i] + ".", "There is a", chance_of_rain_list[i],
          "chance of rain with winds coming from the", wind_list[i] + ".")
    print()
# loop which prints the first 10 days of the forecast in a coherent sentence with variables of the day, date,
# description, high and low temperatures, humidity, chance of rain, and wind.

