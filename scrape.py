import requests,time
from bs4 import BeautifulSoup

url= 'https://www.worldometers.info/coronavirus/country/us/'
page=requests.get(url)
time.sleep(5)
soup=BeautifulSoup(page.content,'html.parser')
results=soup.find("table",attrs={"id":"usa_table_countries_today"})
data=results.tbody.find_all("tr")
f1=open("buf.txt","w")
f2=open("toast.ps1","w")
headings=[]
for td in data[0].find_all("td"):
	headings.append(str(td).translate(str.maketrans('','','<>/td')))
	f1.write(str(td).translate(str.maketrans('','','<>/td')))
	f1.write("\n")
	
f1.close()
f2.close()
print(headings[2])
	

