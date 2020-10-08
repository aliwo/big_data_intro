from datetime import datetime

from crawler.psaw_crawler import psaw_crawler
from model.types import Base
from model.engine import engine, SessionMaker
from model.submission import Submission


if __name__ == '__main__':
    # 모든 테이블을 만듭니다. 처음에 한 번 실행하고 주석처리 하면 됩니다.
    Base.metadata.create_all(engine)
    session = SessionMaker()
    submissions = [Submission(
        title=submission.title,
        submission_id=submission.id,
        author=submission.author.name if submission.author else None,
        selftext=submission.selftext,
        flair=submission.link_flair_text,
        created_at=datetime.utcfromtimestamp(submission.created_utc))
        for submission in psaw_crawler.get_all_in_month(datetime(2017, 1, 1))]
    session.add_all(submissions)
    session.commit()






