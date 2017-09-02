from bs4 import BeautifulSoup

import requests

url = 'https://www.yellowpages.com/search?search_terms=pizza&geo_location_terms=South+India+Mound%2C+Kansas+City%2C+MO'
r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

#print(soup.prettify())

pizza_data = soup.find_all('div', {"class": "info"})
description = soup.find_all('div', {"class": "snippet"})

#print(pizza_data)
#print(description)

pizza_list = []

for item in pizza_data:
	#print(item.contents[0].text)
	#print(item.contents[1].text)
	pizza_list.append(item.contents[0].find_all('a', {"class": "business-name"})[0].text)
	try:
		pizza_list.append(item.contents[1].find_all('span', {"itemprop": "streetAddress"})[0].text)
	except:
		pass
	try:
		pizza_list.append(item.contents[1].find_all('span', {'itemprop': "addressLocality"})[0].text)
	except:
		pass
	try:
		pizza_list.append(item.content[1].find_all('p', {'itemprop': 'address'}[0].text))
	except:
		pass
	try:
		pizza_list.append(item.contents[1].find_all('div', {'itemprop': 'telephone'})[0].text)
	except:
		pass
	try:
		pizza_list.append(item.contents[1].find_all('div', {"class": 'snippet'}))
	except:
		pass
	pizza_list.append('')


pizza_list = [item for item in pizza_list if item != []]
#print(pizza_list)

purified_big_list = [uni.encode('UTF8') for uni in pizza_list]

print(purified_big_list)

pizza_file = open('pizza_data_file.txt','w')

for data in purified_big_list:
	pizza_file.write("%s\n" %data)