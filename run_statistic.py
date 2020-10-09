from datetime import datetime

from sqlalchemy import or_, func

from crawler.libs.date_helper import DateHelper
from model.engine import SessionMaker
from model.submission import Submission
from model.comment import Comment
from model.voca import VOCA
from pandas import DataFrame, Series


session = SessionMaker()
df_map = {
    'dates': [str(year) + str(month).zfill(2) for year in [2017, 2018, 2019]
                            for month in [i for i in range(1, 13)]]
}
# 와! 4중 for 문!
for key, words in VOCA.items():
    temp = []
    for year in [2017, 2018, 2019]:
        for month in [i for i in range(1, 13)]:
            after, before = DateHelper.first2last_date(datetime(year, month, 1))
            result = session.query(Submission).join(Comment)\
                .filter((func.date(Submission.created_at) >= after)
                        &(func.date(Submission.created_at) <= before))\
                .filter(or_(*[(cls.selftext.ilike(f'%{word}%')) for cls in [Submission, Comment] for word in words])).count()
            temp.append(result)

    df_map[key] = temp


df = DataFrame(df_map)
df.to_excel('temp.xlsx')
