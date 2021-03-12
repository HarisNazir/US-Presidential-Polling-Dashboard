from bs4 import BeautifulSoup
import requests

URL = 'https://projects.fivethirtyeight.com/polls/president-general/'

html_data = requests.get(URL)

soup = BeautifulSoup(html_data.content, 'html.parser')

rows = soup.find_all(class_= 'visible-row')

for r in rows:
    date = r.find(class_='date-wrapper').text
    print(date, '\n')

    pollster = r.find(class_='pollster-container')
    pollster_text = pollster.find_all("a")[-1].text

    print(pollster_text, '\n')

    sample_size = r.find(class_='sample').text

    leader = r.find(class_='leader').text
    net = r.find(class_='net').text