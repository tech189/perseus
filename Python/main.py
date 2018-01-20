# This Python file uses the following encoding: utf-8
from bs4 import BeautifulSoup
import urllib.request
import re
from selenium import webdriver
url = "http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0133"
eng_url = "http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0134%3Abook%3D1%3Acard%3D1"
html_soup = BeautifulSoup(urllib.request.urlopen(url).read(),'html.parser')
texts = html_soup.find('div', attrs={'class': 'text_container'}).get_text()
texts = re.sub('\s{2,}',' ', texts)
r = "[]%$£@±^&*+=\{\}"

for character in r:
         texts = texts.replace(character,"")

result = ''.join([i for i in texts if not i.isdigit()])
#print(result)

# Prints all the script tags:
#for a in html_soup.find_all('script'):
    #print("Found the script tag:", a)


# Prints the first part of the array
# print(html_soup.find_all("script")[0])

# Doesn't work why?!??!!?
books = []
for script in html_soup.find_all("script"):
    if re.search("(addDocument\((.+)Perseus(.+))", str(script)):
         regex = re.compile('(?<=addDocument\(\')(.*)(?=\'\);)')
         books.append(regex.findall(str(script))[0])
print(books)
