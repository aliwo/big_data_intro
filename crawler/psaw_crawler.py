import praw
from psaw import PushshiftAPI
from datetime import datetime

__all__ = ['psaw_crawler']

from crawler.libs.date_helper import DateHelper

CLIENT_ID = 'thp4a4sGGUMidA'
CLIENT_SECRET = 'gt6CAnKcJ1eSOqKhfi-8li1gKtk'

if __name__ == '__main__':
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent="my user agent")
    api = PushshiftAPI(reddit)

    gen = api.search_submissions(
        after=int(datetime(2017, 1, 1).timestamp()),
        before=int(datetime(2017, 1, 3).timestamp()), # after 이상, before 미만의 date 가 쿼리 된다.
                                subreddit='acne')
    for submission in gen:
        print(f'{submission.title} {datetime.utcfromtimestamp(submission.created_utc)}')


class Api:

    def __init__(self):
        reddit = praw.Reddit(client_id=CLIENT_ID,
                             client_secret=CLIENT_SECRET,
                             user_agent="my user agent")
        self._api = PushshiftAPI(reddit)


    def get_all_in_month(self, month):
        after, before = DateHelper.first2last_date(month)
        return self._api.search_submissions(
            after=int(after.timestamp()),
            before=int(before.timestamp()),
            subreddit='acne',
            sort='asc')


psaw_crawler = Api()