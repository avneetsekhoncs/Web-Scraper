"""
Practicing Web Scraping by grabbing one element at a time:

Python best practice: Install project packages in its own venv.

Activate virtual env: source "path to activate"
Deactivate venv: Deactivate
"""

import requests
import bs4

"""""""""""""""""""""
Scraping a Title
"""""""""""""""""""""
result = requests.get("https://example.com")
soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup.select("title")[0].getText())        #Return the first title's content

"""""""""""""""""""""
Scraping a Class
"""""""""""""""""""""
grace_hopper = requests.get("https://en.wikipedia.org/wiki/Grace_hopper")
soup = bs4.BeautifulSoup(grace_hopper.text, "lxml")

for item in soup.select(".vector-toc-text"):
    print(item.getText())

"""""""""""""""""""""
Scraping an Image
"""""""""""""""""""""
image = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(image.text, "lxml")

kasparov = soup.select(".thumbimage")[0]
#print(kasparov["src"])
image_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png")
#print(image_link.content)      #This gets the binary file of the image
test_file = open("kasparov_img.png", "wb")      #make sure file extension is the same as the src. Gets saved in working directory
test_file.write(image_link.content)
test_file.close()
