import requests
import bs4 from BeautifulSoup

# trying here for multiple urls
url = ['www.example.com', 'www.example-1.com']

#r to get the request from url string, 
#use_soup to get use bs4, links to store all the a tags that we find
r = requests.get(url)
use_soup = BeautifulSoup(r.content)
links = use_soup.find_all("a")


for link in links:
	print ("<a href ='%s'>%s /a") %(link.get("href"), link.text)

## define variables to store the product informations from the website
get_all_products = use_soup.find_all("section", {"class:" "product"}) ##this will store all the product information from section tag

#calling the conainters-serp class to get each product from the PDP page
# get_each_product = use_soup.find_all("div", {"class:" "container-serp"}) 

for item in get_all_products:
	print(item.text)

##for item in get_each_product:
##	print(item.text)

for item in get_all_products:
	print(item.contents[0].text) ##prints individual product names
	print(item.contents[2].text) #prints third part of the section, second part is called as contents[1], but here it does not have text in it so calling the third part




