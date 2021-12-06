# API key: 172a5c3a01724bbda2cb9ac2cf824816

import requests
from pprint import pprint


class NewsFeed:

    def __init__(self, data):
        self.data = data

    def get(self):
        pass


# Here in the url we use everything end point then parameters are specified.
# You can change the value of q in the url to look for another topic.
# qInTitle looks for the word only in the news title.
# For the full list of parameters visit: https://newsapi.org/docs/endpoints/everything
url = "https://newsapi.org/v2/everything?" \
      "qInTitle=nasa&" \
      "from=2021-12-05&" \
      "to=2021-12-06&" \
      "language=en&" \
      "apiKey=172a5c3a01724bbda2cb9ac2cf824816"

response = requests.get(url)
content = response.json()  # The response is in json format and will be converted to dictionary
# x = content['articles'][2]['title']  # Title of the 3rd article
# y = content['articles'][2]['url']  # url of the 3rd article
# pprint(x)
# pprint(y)

articles = content['articles']

email_body = ''
for article in articles:
    email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

print(email_body)
