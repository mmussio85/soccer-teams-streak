import requests
from bs4 import BeautifulSoup

URL = 'https://www.sobrefutbol.com/torneos/torneo_uruguayo.htm'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
columns = soup.find("div", {"class": "rd-tbl-2"}).find("tr", {"class": "t-enc-2 a-left"}).find_all("b")
header = ",".join(map(lambda x: x.text, columns)) + "\n"

values = soup.find_all("div", {"class": "rd-tbl-2"})
rows = []
for i in values:
	rows.extend(i.find_all("tr", {"valign": "top"}))

result = [i.findChildren("td" , recursive=False) for i in rows]
plain_td = [[field.text.strip().replace("\n","").replace("\t","") for field in r if field.text] for r in result]

values_text = ""
for row in plain_td:
	values_text = values_text + ",".join(row)  + "\n"

text_file = open("championships.csv", "w")
n = text_file.write(header + values_text)
text_file.close()
