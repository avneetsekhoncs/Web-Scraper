"""
Python best practice: Install project packages in its own venv.

Activate venv: source .venv/Scripts/activate
Deactivate venv: Deactivate
"""

import requests
import bs4

result = requests.get("https://example.com")
#print(result) returns <Response [200]>

soup = bs4.BeautifulSoup(result.text, "lxml")
# print(soup) returns the html of website
soupTitle = soup.select("title")
# print(soupTitle) return the specified tags with their content
print(soupTitle[0].getText()) #Return the first title's content