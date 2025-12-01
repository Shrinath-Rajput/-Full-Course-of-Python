from bs4 import BeautifulSoup

soup=BeautifulSoup("<html> <p>) Shrinath <strong> Hello <a> Hello </html","html.parser")
print(soup.pr)
