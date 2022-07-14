from bs4 import BeautifulSoup as bs
import requests
import csv
import pandas as pd

bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(bright_stars_url)
soup = bs(page.text, 'html.parser')
star_table = soup.find('table')

temp_list = []
table_rows = star_table.find_all('tr')

for tr in table_rows:
  td = tr.find_all('td')
  row = [i.text.rstrip()for i in td]
  temp_list.append(row)

Star_names = []
Distance = []
Mass = []
Radius = []

for i in range(1,len(temp_list)) :
  Star_names.append(temp_list[i][1])
  Distance.append(temp_list[i][3])
  Mass.append(temp_list[i][5])
  Radius.append(temp_list[i][6])

df2 = pd.Dataframe(list(zip(Star_names, Distance, Mass, Radius)),columns = ['Star_names', 'Distance', 'Mass', 'Radius'])
print(df2)
df2.to_csv('dwarf_stars.csv')