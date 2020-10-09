from datetime import datetime

from sqlalchemy import or_, func

from crawler.libs.date_helper import DateHelper
from model.engine import SessionMaker
from model.submission import Submission
from model.comment import Comment
from model.voca import VOCA
from pandas import DataFrame, Series

strategy = '''
그냥 돌아가면서 쿼리해도 충분함... 3만개 row 를 대상으로, 쿼리 하나에 1초도 안 걸린다. 현재 30MB (2017 ~ 2019)
일단 지금 데이터를 늘릴 필요는 없겠지만, 나중에는 2015년 부터 쭉 모으자.

모든 voca 의 언급횟수를 "월 별" 로 추려내서 어딘가에 저장할 거다. pandas 로 저장해서 csv 로 뽑아?
'''

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
