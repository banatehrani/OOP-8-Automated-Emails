import yagmail
import pandas
from news import NewsFeed

df = pandas.read_excel('people.xlsx')

for index, row in df.iterrows():
    news_feed = NewsFeed(interest=row['interest'],
                         from_date='2021-12-05',
                         to_date='2021-12-06')

    yagmail.SMTP(user="mehdi.python.developer@gmail.com", password="mehdi_python_developer"). \
        send(to=row['email'],
             subject=f"{row['interest']} news for today!",
             contents=f"Hi {row['name']}\n See what's new about {row['interest']} "
                      f"today. {news_feed.get()}\nPython Developer")
