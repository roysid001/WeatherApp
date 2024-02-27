import requests
from bs4 import BeautifulSoup

search = "weather in mumbai"
url = f"https://www.google.com/search?&q={search}"
r = requests.get(url)
s = BeautifulSoup(r.text, "html.parser")
update = s.find("div", class_="BNeawe iBp4i AP7Wnd").text
print(update)