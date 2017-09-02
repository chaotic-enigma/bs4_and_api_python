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
	print

print(pizza_list)

desc_data = []
for desc in description:
	desc_data.append(("people's opinion --> %s") % desc.text)
print

print(desc_data)

print

burger = zip(pizza_list, desc_data)

print(burger)

nes_list = []

for tu in burger:
	nes_list.append(list(tu))

for single_list in nes_list:
	single_list.append('')

#print(nes_list)

big_list = []

for sublist in nes_list:
	for single_item in sublist:
		big_list.append(single_item)

#print(big_list)

purified_big_list = [uni.encode('UTF8') for uni in big_list]

#print(purified_big_list)

pizza_file = open('pizza_shop_reviews.txt','w')

for data in purified_big_list:
	pizza_file.write("%s\n" %data)