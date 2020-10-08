
# comment 까지 저장할 거라면 부모와 자식 comment 까지 저장해야 함...

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.mysql import CHAR, TEXT, DATETIME
from model.types import Base


class Comment(Base):
    __tablename__ = 'comments'
    submission_id = Column(Integer, ForeignKey('submissions.id'))
    unique_id = Column(CHAR(15))
    author = Column(TEXT)
    selftext = Column(TEXT)
    created_at = Column(DATETIME)

    def json(self):
        return {
            'submission_id': self.submission_id,
            'author': self.author,
            'selftext': self.selftext,
            'created_at': self.created_at,
        }
