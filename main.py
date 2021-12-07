import yagmail
import pandas as pd
import datetime
import time
from news import NewsFeed

while True:
    if datetime.datetime.now().hour == 20 and datetime.datetime.now().minute == 38:

        df = pd.read_excel('people.xlsx')

        for index, row in df.iterrows():
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            yesterday = ((datetime.datetime.now() -
                          datetime.timedelta(days=1)).strftime('%Y-%m-%d'))
            news_feed = NewsFeed(interest=row['interest'],
                                 from_date=yesterday,
                                 to_date=today)

            yagmail.SMTP(user="mehdi.python.developer@gmail.com", password="mehdi_python_developer"). \
                send(to=row['email'],
                     subject=f"{row['interest']} news for today!",
                     contents=f"Hi {row['name']}\n See what's new about {row['interest']} "
                              f"today. {news_feed.get()}\nPython Developer")

    time.sleep(60)
