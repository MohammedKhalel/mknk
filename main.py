import requests
from bs4 import BeautifulSoup
jop_title = []
company_name = []
location = []
skill = []
link = []
date =[]

result = requests.get("https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=java%20developer")
src = result.content

soup = BeautifulSoup(src, "lxml")

jop_titles= soup.find_all("h2",{"class":"css-m604qf"})
company_names= soup.find_all("a",{"class":"css-17s97q8"})
locations= soup.find_all("span",{"class":"css-5wys0k"})
jop_skills= soup.find_all ("div",{"class":"css-y4udm8"})
early_published = soup.find_all("div",{"class":"css-4c4ojb"})
old_published = soup.find_all("div",{"class":"css-do6t5g"})
published = [*early_published, *old_published]
for i in range(len(jop_titles)):
 jop_title.append(jop_titles[i].text)
 link.append(jop_titles[i].find("a").attrs['href'])
 company_name.append(company_names[i].text)
 location.append(locations[i].text)
 skill.append(jop_skills[i].text)
 date.append(published[i].text)
 print(jop_title , company_name ,location , skill , link , date )