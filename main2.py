from bs4 import BeautifulSoup
import requests
import csv
import numpy as np

def getDataSetURL(file_name):
    url = []
    i = 0
    with open(file_name) as filecsv:
        reader = csv.reader(filecsv, delimiter=',')
        for row in reader:
            if i != 0:
                url.append(str(row[0]))
            i += 1

    return url

page_link = getDataSetURL('DataSetArtikel.csv')

article = []
for data in page_link:
    page_response = requests.get(data, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    findP = page_content.find_all("p")

    textContent = []
    for i in range(0, len(findP)):
        paragraphs = findP[i].text
        textContent.append(paragraphs)

    a = []
    i = 0
    findAt = 0
    for data in textContent:
        if 'Klikdokter.com' in data:
            findAt = i
        i += 1

    for i in range(findAt, len(textContent)):
        a.append(textContent[i])

    article.append(a)

np.savetxt('article.txt', article, fmt="%s")