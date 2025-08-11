import requests
from bs4 import BeautifulSoup
import json
#git config --global user.name "Aakash Gharti Magar"

# install git
# create repository in github

#go to git bash
# git config --global user.name "Aakash Gharti Magar"
# git config --global user.email "hdaash@gmail.com"

# git init
# git status => if you want to check what are the status of files
# git diff => if you want to check what are the changes
# git add .
# git commit -m your message
# copy paste git code from github

########
# 1. code change
# 2. git add .
# 3. git commit -m "Your mw=essage"
# 4. git push
########


URL = "https://books.toscrape.com/"

def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the page")
        return
    
    
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_= "product_pod")
    book_list = []
    for book in books:
        title = book.h3.a["title"]
        price_text = book.find("p", class_="price_color").text
        currency = price_text[0]
        price = price_text[1:]
        book_list.append({"title":title, "currency": currency, "price":price})
    return book_list







books = scrape_books(URL)
with open("books.json", "w") as f:
    json.dump(books, f, indent=2, ensure_ascii = False)