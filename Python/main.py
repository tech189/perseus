# This Python file uses the following encoding: utf-8
from bs4 import BeautifulSoup
import urllib.request
import re, ast, sys
import mysql.connector

def printText(url):
    texts = html_soup.find('div', attrs={'class': 'text_container'}).get_text()
    texts = re.sub('\s{2,}',' ', texts)
    r = "[]%$£@±^&*+=\{\}"

    for character in r:
        texts = texts.replace(character,"")

    result = ''.join([i for i in texts if not i.isdigit()])
    print(result)

    connection = mysql.connector.connect(user="root", password="root", host="localhost", database="perseus")
    cursor = connection.cursor()
    #add_text = "INSERT INTO texts (text_content) VALUES (%s)"
    cursor.execute("INSERT INTO texts (text_content) VALUES ('%s')", result)
    connection.commit()
    print("Added to texts table")

def printRelatedBooks(url):
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
    while (i < len(bks.keys())):
        print(list(bks.keys())[i] + " : " + bks[list(bks.keys())[i]])
        i = i + 1

def readDatabase():
    connection = mysql.connector.connect(user="root", password="root", host="localhost", database="perseus")
    cursor = connection.cursor()
    cursor.execute("SELECT text_id, text_title FROM texts")
    row = cursor.fetchone()

    if row is None:
        print("Empty texts table")
    while row is not None:
        print(row[0], row[1])
        row = cursor.fetchone()

    cursor.close()
    connection.close()


help_text = "Perseus scraper\nArguments:\n\t-d\tDemo text (Homer's Iliad Book 1 Line 1)\n\t-u\tScrapes a specific url\n\t-t\tTests the database"

if len(sys.argv) < 2:
    print(help_text)
elif sys.argv[1] == "-d":
    url ="http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0133"
    html_soup = BeautifulSoup(urllib.request.urlopen(url).read(),'html.parser')
    printText(url)
   # printRelatedBooks(url)
elif sys.argv[1] == "-u":
    url = sys.argv[2]
    html_soup = BeautifulSoup(urllib.request.urlopen(url).read(),'html.parser')
    printText(url)
    printRelatedBooks(url)
elif sys.argv[1] == "-t":
    readDatabase()
else:
    print(help_text)





