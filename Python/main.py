from bs4 import BeautifulSoup
import urllib.request
import re
url = "http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0133"
eng_url = "http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0134%3Abook%3D1%3Acard%3D1"
html_soup = BeautifulSoup(urllib.request.urlopen(url).read(),'html.parser')
texts = html_soup.find('div', attrs={'class': 'text_container'}).get_text().replace('\n','')
texts = re.sub('\s{2,}',' ', texts)
r = "[]"

for character in r:
         texts = texts.replace(character,"")

result = ''.join([i for i in texts if not i.isdigit()])
print(result)
