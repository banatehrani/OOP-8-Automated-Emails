import requests
import datetime


class NewsFeed:
    """Representing multiple news titles and links as a single string"""

    base_url = "https://newsapi.org/v2/everything?"
    api_key = "172a5c3a01724bbda2cb9ac2cf824816"

    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
        return url


if __name__ == "__main__":
    news_feed = NewsFeed(interest='nasa',
                         from_date=((datetime.datetime.now() -
                                     datetime.timedelta(days=1)).strftime('%Y-%m-%d')),
                         to_date=datetime.datetime.now().strftime('%Y-%m-%d'),
                         language='en')
    print(news_feed.get())

# Here in the url we use everything end point then parameters are specified.
# You can change the value of q in the url to look for another topic.
# qInTitle looks for the word only in the news title.
# For the full list of parameters visit: https://newsapi.org/docs/endpoints/everything
# url = "https://newsapi.org/v2/everything?" \
#       "qInTitle=nasa&" \
#       "from=2021-12-05&" \
#       "to=2021-12-06&" \
#       "language=en&" \
#       "apiKey=172a5c3a01724bbda2cb9ac2cf824816"
#
# response = requests.get(url)
# content = response.json()  # The response is in json format and will be converted to dictionary
# x = content['articles'][2]['title']  # Title of the 3rd article
# y = content['articles'][2]['url']  # url of the 3rd article
# pprint(x)
# pprint(y)
#
# articles = content['articles']
#
# email_body = ''
# for article in articles:
#     email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"
#
# print(email_body)
