#****************************************************************
#Name: Wing Lok LO
#Link: https://replit.com/join/adqcqhwghw-lowinglokjason
#****************************************************************

import requests
from bs4 import BeautifulSoup

# get my website URL 
response = requests.get("https://module-1-build-and-scrape-a-website-about-yourself.lowinglokjason.repl.co")

# create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# find the p tag
tags = soup.select('p')

# specify the path to save the results
path = "file.txt"

# save the results
with open(path, "w") as file:
  for tag in tags:
    data = tag.get_text(strip=True)  # extract the text content of p tag
    file.write(data + "\n")
# done
print(f"Scraped data saved to {path}")


# download the files from my website and save them in myresume.pdf
import requests
url = 'https://module-1-build-and-scrape-a-website-about-yourself.lowinglokjason.repl.co/doc/WING_LOK_LO_CV_2023.pdf'
r = requests.get(url, allow_redirects=True)
open('myresume.pdf', 'wb').write(r.content)