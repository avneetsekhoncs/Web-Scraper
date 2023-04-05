"""
Purpose of this script: Get the title of every book with a two star rating

Website: http://books.toscrape.com/catalogue/page-1.html
"""

import requests
import bs4

print("Checking if the first book on this specified page has a two star rating...")

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
response = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(response.text, "lxml")
book_list = soup.select(".product_pod")

check_book = book_list[0]
if check_book.select(".star-rating.Two") == []:     #.star-rating Two => .star-rating.Two
    print("It is not two stars")
    print("")
else:
    first_title = check_book.select("a")[1]["title"]       #check_book is of type '<class 'bs4.element.Tag'>' which works like a disctionary
    print(first_title)
    print("")


print("Getting a list of book titles with two star ratings from pages 1 through 50 ...")

two_star_titles = []

for i in range(1,51):
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    response = requests.get(base_url.format(i))
    soup = bs4.BeautifulSoup(response.text, "lxml")
    book_list = soup.select(".product_pod")

    for book in book_list:
        if len(book.select(".star-rating.Two")) != 0:
            book_title = book.select("a")[1]["title"]
            two_star_titles.append(book_title)

print("\n".join(two_star_titles))       #'join()' will concatenate the string with a newline character in between them
