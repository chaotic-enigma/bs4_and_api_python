from bs4 import BeautifulSoup

import requests

url = 'https://www.yellowpages.com/los-angeles-ca/coffee?g=los%20angeles%2C%20ca&q=coffee'
r = requests.get(url)


soup = BeautifulSoup(r.content, "lxml")

#print(soup.prettify())

links = soup.find_all("a")

g_data = soup.find_all("div", {"class":"info"})
#print(g_data)

coffee_data = []

for item in g_data:
	#print(item.contents[0].text)
	#print(item.contents[1].text)

	coffee_data.append(item.contents[0].find_all("a", {"class": "business-name"})[0].text)
	#print item.contents[1].find_all("p", {"class": "adr"})[0].text
	try:
		coffee_data.append(item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text)
	except:
		pass
	try:
		#print item.contents[1].find_all("span", {"class": "address"})[0].text
		coffee_data.append(item.contents[1].find_all("span", {"itemprop": "addressLocality"})[0].text.replpace(',',''))
	except:
		pass
	try:
		coffee_data.append(item.contents[1].find_all("span", {"itemprop": "addressRegion"})[0].text)
	except:
		pass
	try:
		coffee_data.append(item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text)
	except:
		pass
	try:
		coffee_data.append(item.contents[1].find_all("li", {"itemprop": "primary"})[0].text)
	except:
		pass
	coffee_data.append('')

print coffee_data

coffee_file = open('coffee_data_file.txt','w')

for data in coffee_data:
	coffee_file.write("%s\n" % data)