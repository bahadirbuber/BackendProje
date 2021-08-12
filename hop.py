import requests
from bs4 import BeautifulSoup
URL = "https://www.etsy.com/uk/listing/772695061/brass-or-silver-leaf-bookmark-set"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))

print(images)

