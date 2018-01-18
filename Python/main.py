from bs4 import BeautifulSoup
import urllib2

url = "http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0133"
html_soup = BeautifulSoup(urllib2.urlopen(url).read(),'html.parser')
texts = html_soup.find('div', attrs={'class': 'text_container'}).get_text()

print texts
