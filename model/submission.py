from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import CHAR, BOOLEAN, TEXT, DECIMAL, DATETIME
from sqlalchemy.orm import relationship

from model.types import Base


class Submission(Base):
    __tablename__ = 'submissions'
    unique_id = Column(CHAR(15))
    title = Column(TEXT)
    author = Column(TEXT)
    selftext = Column(TEXT)
    flair = Column(TEXT)
    created_at = Column(DATETIME)

    comments = relationship('Comment')

    def json(self):
        return {
            'title': self.title,
            'unique_id': self.unique_id,
            'author': self.author,
            'selftext': self.selftext,
            'flair': self.flair,
            'created_at': self.created_at,
        }
