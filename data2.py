from bs4 import BeautifulSoup as bs
import requests
import pandas as pd 

url="https://en.wikipedia.org/wiki/Lists_of_stars"

page=requests.get(url)
soup=bs(page.text,'html.parser')
star_table=soup.find_all('table')

table_rows=star_table.find_all("tr")
temp_list=[]
for tr in table_rows:
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)

star_names=[]
distance=[]
mass=[]
radius=[]
lum=[]

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    lum.append(temp_list[i][7])

df2=pd.DataFrame(list(zip(star_names,distance,mass,radius,lum)),columns=['star_names','distance','mass','radius','lum'])
df2.to_csv("brightest_stars.csv")

