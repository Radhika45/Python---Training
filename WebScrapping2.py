#Sports Team Data Web Scrapping
import requests
from bs4 import BeautifulSoup
url = "https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/points-table-standings"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

teams = soup.find_all('span' , class_ = "ds-text-tight-s ds-font-bold ds-uppercase ds-text-left ds-text-typo")
wins = soup.find_all('th', class_ = "ds-w-0 ds-whitespace-nowrap ds-min-w-max")

data = []

for idx in range(10):
    team_data = dict()
    team_data['name']= ""
    team_data['stats'] = []
    data.append(team_data)

print("Data: ",data)

idx = 0
for team in teams:
    title = team.text.strip()
    data[idx]['name'] = title
    idx = +1

print("data: ",data)

team_idx =0
idx = 0
for win in wins:
    num = win.text.strip()
    print(num)
    idx += 1
    if idx % 8 == 0:
        print("wow...")



"""
team_idx = 0
idx = 0
for win in wins:
    num = win.text.strip()
    print(num)
    idx += 1
    if idx % 8 == 0:
        print("Wow.....")"""