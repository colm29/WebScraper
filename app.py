import requests
from bs4 import BeautifulSoup

response = requests.get('https://stackoverflow.com/questions')
soup = BeautifulSoup(response.text, 'html.parser')

questions = soup.select('.question-summary')
for question in questions:
    print(question.select_one('.question-hyperlink').getText())
    print('Votes', question.select_one('.vote-count-post').getText())

# For multiple pages find pagination component within HTML and run above code in each page
