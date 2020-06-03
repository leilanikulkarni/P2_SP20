# FINAL
# because I did my work in the python console, I attached all my work in docstrings below.
'''
First Question:
import pandas as pd
import matplotlib.pyplot as plt  # importing libraries
Backend MacOSX is interactive backend. Turning interactive mode on.
df = pd.read_csv('/Users/leilanikulkarni/PycharmProjects/P2_SP20/final copy/climate-change-computer-programming-final/countries.csv')  # importing data set
df.columns  # seeing which columns I need to analyze
Out[5]:
Index(['Country', 'Region', 'Population (millions)', 'HDI', 'GDP per Capita',
       'Cropland Footprint', 'Grazing Footprint', 'Forest Footprint',
       'Carbon Footprint', 'Fish Footprint', 'Total Ecological Footprint',
       'Cropland', 'Grazing Land', 'Forest Land', 'Fishing Water',
       'Urban Land', 'Total Biocapacity', 'Biocapacity Deficit or Reserve',
       'Earths Required', 'Countries Required', 'Data Quality'],
      dtype='object')
graph = df.plot.scatter('Population (millions)', 'Total Ecological Footprint', title='Population vs. Total Ecological Footprint')
df.groupby(['Population (millions)'])['Total Ecological Footprint'].mean()  # getting the specific data for the US
Out[7]:
Population (millions)
0.00       7.780
0.01       2.505
0.03       2.860
0.05       4.940
0.06       5.710
           ...
198.66     3.110
246.86     1.580
317.50     8.220
1236.69    1.160
1408.04    3.380
Name: Total Ecological Footprint, Length: 179, dtype: float64
graph.annotate("United States of America", xy=(317.5, 8.220))  # annotating the US onto the graph
Out[8]: Text(317.5, 8.22, 'United States of America')
'''

'''
SECOND QUESTION:
import pandas as pd
import matplotlib.pyplot as plt  # importing libraries
Backend MacOSX is interactive backend. Turning interactive mode on.
df = pd.read_csv('/Users/leilanikulkarni/PycharmProjects/P2_SP20/final copy/climate-change-computer-programming-final/countries.csv')  # importing data set
df.columns  # seeing which columns I want to analyze
Out[5]: 
Index(['Country', 'Region', 'Population (millions)', 'HDI', 'GDP per Capita',
       'Cropland Footprint', 'Grazing Footprint', 'Forest Footprint',
       'Carbon Footprint', 'Fish Footprint', 'Total Ecological Footprint',
       'Cropland', 'Grazing Land', 'Forest Land', 'Fishing Water',
       'Urban Land', 'Total Biocapacity', 'Biocapacity Deficit or Reserve',
       'Earths Required', 'Countries Required', 'Data Quality'],
      dtype='object')
df['Earths Required'].max()  # finding the value with the highest Earths required to keep up with the resources it's using
Out[6]: 9.14
df.loc[df['Earths Required'] == 9.14]  # finding which country has this value
Out[7]: 
        Country          Region  ...  Countries Required  Data Quality
102  Luxembourg  European Union  ...                9.44             5
[1 rows x 21 columns]
df['Earths Required'].min()  # finding the value with the lowest Earths required to keep up the resources it's using
Out[8]: 0.24
df.loc[df['Earths Required'] == 0.24]  # finding the country that has this value
Out[9]: 
    Country  Region  ...  Countries Required  Data Quality
56  Eritrea  Africa  ...                0.32             5
[1 rows x 21 columns]
# Luxembourg requires the most Earths (9.14) while Eritrea requires the least (0.24)
'''

'''
THIRD QUESTION:
import pandas as pd
import matplotlib.pyplot as plt  # importing libraries
Backend MacOSX is interactive backend. Turning interactive mode on.
df = pd.read_csv('/Users/leilanikulkarni/PycharmProjects/P2_SP20/final copy/climate-change-computer-programming-final/countries.csv')  # importing data set
df.columns  # seeing which columns I want to analyze
Out[5]: 
Index(['Country', 'Region', 'Population (millions)', 'HDI', 'GDP per Capita',
       'Cropland Footprint', 'Grazing Footprint', 'Forest Footprint',
       'Carbon Footprint', 'Fish Footprint', 'Total Ecological Footprint',
       'Cropland', 'Grazing Land', 'Forest Land', 'Fishing Water',
       'Urban Land', 'Total Biocapacity', 'Biocapacity Deficit or Reserve',
       'Earths Required', 'Countries Required', 'Data Quality'],
      dtype='object')
grouped = df.groupby(['Country', 'Grazing Land'])['Grazing Footprint'].mean()  # making a variable for the columns I want to analyze
grouped['Luxembourg']  # finding the necessary information for Luxembourg
Out[7]: 
Grazing Land
0.08    0.76
Name: Grazing Footprint, dtype: float64
# found that grazing land (0.08) is much less than grazing footprint (0.76)
grouped['Eritrea']  # finding the necessary information for Eritrea
Out[9]: 
Grazing Land
0.18    0.18
Name: Grazing Footprint, dtype: float64
# grazing land and grazing footprint are the same which is good
df.plot.scatter('Grazing Land', 'Grazing Footprint', title='Grazing Land vs. Grazing Footprint')  # making the graph
Out[11]: <matplotlib.axes._subplots.AxesSubplot at 0x7facc2348978>
graph = df.plot.scatter('Grazing Land', 'Grazing Footprint', title='Grazing Land vs. Grazing Footprint')  # making a variable for it
graph.annotate("Luxembourg", xy=(0.08, 0.76))  # annotating Luxembourg to see where it stands in comparison to other countries
Out[13]: Text(0.08, 0.76, 'Luxembourg')
graph.annotate("Eritrea", xy=(0.18, 0.18))  # annotating Eritrea to see where it stands in comparison to other countries
Out[14]: Text(0.18, 0.18, 'Eritrea')
'''