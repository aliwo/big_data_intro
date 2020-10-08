from datetime import datetime

import praw

# 내 reddit app 조회 하기:
# https://www.reddit.com/prefs/apps
CLIENT_ID = 'thp4a4sGGUMidA'
CLIENT_SECRET = 'gt6CAnKcJ1eSOqKhfi-8li1gKtk'


# 특정 년도의, success storty flair 를 가진 모든 submission 을 조회하려면? 이걸 직렬화 해서 elasticsearch 에 넣을까?
if __name__ == '__main__':
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent="my user agent")
    i = 0
    for submission in reddit.subreddit("acne").search('flair:"Success Story"'):
        i += 1

    print(f'{submission.title} {submission.link_flair_text} {datetime.utcfromtimestamp(submission.created_utc)}')
    print(i)