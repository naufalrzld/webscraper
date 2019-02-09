from bs4 import BeautifulSoup
import requests
import csv

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

url = getDataSetURL('DataSetArtikel.csv')

article = []

for data in url:
    page_response = requests.get(data, timeout=5)
    
    page_content = BeautifulSoup(page_response.content, "html.parser")
    div = page_content.find_all("div", class_="article-content-body__item-page")

    article.append(div[0].text)

print(article[0])

print(nltk.word_tokenize(article[0]))

text_file = open("article.txt", "w")
text_file.write("Purchase Amount: %s" % article)
text_file.close()


#we use the html parser to parse the url content and store it in a variable.
#print(len(page_content.find_all("p")))

# textContent = []
# for i in range(0, len(div.find_all("p"))):
#     paragraphs = page_content.find_all("p")[i].text
#     textContent.append(paragraphs)

#print(textContent)