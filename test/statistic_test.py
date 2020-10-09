from datetime import datetime

from sqlalchemy import func, or_

from crawler.libs.date_helper import DateHelper
from model.comment import Comment
from model.engine import SessionMaker
from model.submission import Submission
from model.voca import VOCA
from pandas import DataFrame, Series


def test_statistic_query():
    session = SessionMaker()
    words = VOCA['adapalen']
    after, before = DateHelper.first2last_date(datetime(2017, 2, 1))
    result = session.query(Submission).join(Comment) \
        .filter((func.date(Submission.created_at) >= after)
                & (func.date(Submission.created_at) <= before)) \
        .filter(or_(*[(cls.selftext.ilike(f'%{word}%')) for cls in [Submission, Comment] for word in words])).all()
    print(result)
    assert False


def test_append_df():
    df = DataFrame(columns=['item'] +
                           [str(year) + str(month).zfill(2) for year in [2017, 2018, 2019]
                            for month in [i for i in range(1, 13)]]
                   )
    df = df.append(Series(['benzoyl'] + [str(year) + str(month).zfill(2) for year in [2017, 2018, 2019]
                            for month in [i for i in range(1, 13)]], index=df.columns), ignore_index=True)
    print(df)