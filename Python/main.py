# This Python file uses the following encoding: utf-8
from bs4 import BeautifulSoup
import urllib.request
import re, ast

if input("Demo text? (y/n) ").upper() == "Y":
    url ="http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0133"
else:
    url = input("Type in a perseus url: \n")

html_soup = BeautifulSoup(urllib.request.urlopen(url).read(),'html.parser')

def printText(url):
    texts = html_soup.find('div', attrs={'class': 'text_container'}).get_text()
    texts = re.sub('\s{2,}',' ', texts)
    r = "[]%$£@±^&*+=\{\}"

    for character in r:
        texts = texts.replace(character,"")

    result = ''.join([i for i in texts if not i.isdigit()])

    print(result)

def printRelatedBooks(url):
    books = {}
    for script in html_soup.find_all("script"):

        if re.search("(addDocument\((.+)Perseus(.+))", str(script)):
            regex = re.compile('(?<=addDocument\(\')(.*)(?=\'\);)')
            #books.append(regex.findall(str(script))[0])
            other_book_url = "http://www.perseus.tufts.edu/hopper/text?doc=" + regex.findall(str(script))[0]
            other_book_soup = BeautifulSoup(urllib.request.urlopen(other_book_url).read(),"html.parser")
            title = other_book_soup.find("div", attrs={"id": "header_text"}).get_text().replace("\n", "").replace("&apos;", "'")

            rek = re.compile('(?<=\w)(\\t)(?=\w)')
            title = rek.sub(' ', title)

            zcy = re.compile('(\\t)')
            title = zcy.sub('', title)

            books[title] = other_book_url


    bks = ast.literal_eval(str(books))
    i = 0
    while (i < len(bks.keys())):
        print(list(bks.keys())[i] + " : " + bks[list(bks.keys())[i]])
        i = i + 1

printText(url)
printRelatedBooks(url)
