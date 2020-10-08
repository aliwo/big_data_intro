from datetime import datetime

from crawler.psaw_crawler import psaw_crawler
from model.comment import Comment
from model.engine import SessionMaker
from model.submission import Submission


class Controller:

    def __init__(self):
        self.session = SessionMaker()

    def save_all_in_month(self, year, month):
        '''
        comment 는 top level comment 만 가져옵니다.
        '''
        query_result = list(psaw_crawler.get_all_in_month(datetime(year, month, 1)))
        submissions = [Submission(
            title=submission.title,
            unique_id=submission.id,
            author=submission.author.name if submission.author else None,
            selftext=submission.selftext,
            flair=submission.link_flair_text,
            created_at=datetime.utcfromtimestamp(submission.created_utc))
            for submission in query_result]
        self.session.add_all(submissions)
        self.session.flush()

        submission_map = {submission.unique_id: submission for submission in submissions}
        comments = [Comment(
            submission_id=submission_map[elem.id].id,
            unique_id=com.id,
            author=com.author.name if com.author else None,
            selftext=com.body,
            created_at=datetime.utcfromtimestamp(com.created_utc))
            for elem in query_result for com in elem.comments]

        self.session.add_all(comments)

    def commit(self):
        self.session.commit()

