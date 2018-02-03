# This Python file uses the following encoding: utf-8
from bs4 import BeautifulSoup
import urllib.request
import re, ast, sys
import mysql.connector

text_content = ""
text_title = ""
related_texts = ""

def getTextContent(url):
    texts = html_soup.find('div', attrs={'class': 'text_container'}).get_text()
    texts = re.sub('\s{2,}',' ', texts)
    r = "[]%$£@±^&*+=\{\}"

    for character in r:
        texts = texts.replace(character,"")

    result = ''.join([i for i in texts if not i.isdigit()])
    text_content = result

    print("The content of the text: " + result)

def getTextTitle(url):
    title = html_soup.title.string

    print("Title is:" + title)

def getRelatedTexts(url):
    books = {}
    for script in html_soup.find_all("script"):

        if re.search("(addDocument\((.+)Perseus(.+))", str(script)):
            regex = re.compile('(?<=addDocument\(\')(.*)(?=\'\);)')
            #books.append(regex.findall(str(script))[0])
            other_book_url = "http://www.perseus.tufts.edu/hopper/text?doc=" + regex.findall(str(script))[0]
            other_book_soup = BeautifulSoup(urllib.request.urlopen(other_book_url).read(),"html.parser")
            title = other_book_soup.find("div", attrs={"id": "header_text"}).get_text().replace("\n", "").replace("&apos;", "'")

            regex2 = re.compile('(?<=\w)(\\t)(?=\w)')
            title = regex2.sub(' ', title)

            regex3 = re.compile('(\\t)')
            title = regex3.sub('', title)

            books[title] = other_book_url


    bks = ast.literal_eval(str(books))
    i = 0
    print("\nRelated books:")
    while (i < len(bks.keys())):
        print(list(bks.keys())[i] + " : " + bks[list(bks.keys())[i]])
        i = i + 1

    related_texts = bks

def insertData(text_title, text_content, related_texts):
    connection = mysql.connector.connect(user="root", password="root", host="localhost", database="perseus")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO texts (text_link, text_title, text_content, related_texts_links) VALUES ('%s', '%s', '%s', '%s')" %(url, text_title, text_content, related_texts))
    connection.commit()

    print("Added to texts table")

    cursor.close()
    connection.close()

def readDatabase():
    connection = mysql.connector.connect(user="root", password="root", host="localhost", database="perseus")
    cursor = connection.cursor()
    cursor.execute("SELECT text_id, text_title, text_content FROM texts")
    row = cursor.fetchone()

    if row is None:
        print("Empty texts table")
    while row is not None:
        print(row[0], row[1], row[2])
        row = cursor.fetchone()

    cursor.close()
    connection.close()


help_text = "Perseus scraper\nArguments:\n\t-d\tScrapes the demo text (Homer's Iliad Book 1 Line 1)\n\t-u\tScrapes a specific url\n\t-t\tTests the database, prints out texts table"

if len(sys.argv) < 2:
    print(help_text)
elif sys.argv[1] == "-d":
    url ="http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0133"
    html_soup = BeautifulSoup(urllib.request.urlopen(url).read(),'html.parser')
    getTextTitle(url)
    getTextContent(url)
    getRelatedTexts(url)
    insertData(text_title, text_content, related_texts)

elif sys.argv[1] == "-u":
    url = sys.argv[2]
    html_soup = BeautifulSoup(urllib.request.urlopen(url).read(),'html.parser')
    getTextTitle(url)
    getTextContent(url)
    getRelatedTexts(url)
elif sys.argv[1] == "-t":
    readDatabase()
else:
    print(help_text)





