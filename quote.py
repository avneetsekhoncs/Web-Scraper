"""
Task: Scrape information from quotes.toscrape.com
"""
#Libraries
import requests
import bs4

#Get HTML text
main_url = "https://quotes.toscrape.com"
response = requests.get(main_url)
soup = bs4.BeautifulSoup(response.text, "lxml")

#Get unique names of authors on the first page
authors = set()
for author in soup.select(".author"):
    authors.add(author.text)

#Create a list of all the quotes on first page
quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)

#Extract top ten tags from the home page
ten_tags = []
for tag in soup.select(".tag-item"):
    ten_tags.append(tag.text)

#Get all the unique authors on the website
all_authors = set()
page = 1

while True:
    url = "https://quotes.toscrape.com/page/{}"
    response = requests.get(url.format(page))
    soup = bs4.BeautifulSoup(response.text, "lxml")
    
    if soup.select(".quote") == []:
        break
    
    for author_name in soup.select(".author"):
        all_authors.add(author_name.text)

    page+=1

print(all_authors)