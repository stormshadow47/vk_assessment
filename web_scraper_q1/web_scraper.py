import requests
from bs4 import BeautifulSoup

r = requests.get("https://theatlantic.com")


if r.status_code == 200:

    soup = BeautifulSoup(r.text, "html5lib")

    articles = soup.find_all("article")

    for i, article in enumerate(articles):
        header = article.select_one("h1 a, h2 a, h3 a")
        
        if header:
            title = header.get_text().strip()
            
            url = header['href']
            if url.startswith('/'):
                url = 'https://theatlanticcom' + url

            print(f"{i + 1}. Title: {title}")
            print(f"   URL: {url}")
            print("-" * 50)
else:
    print(f"Failed to retrieve the page. Status code: {r.status_code}")

