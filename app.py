from bs4 import BeautifulSoup
import requests

URL = 'https://projects.fivethirtyeight.com/polls/president-general/'

html_data = requests.get(URL)

soup = BeautifulSoup(html_data.content, 'html.parser')

print(soup.prettify())