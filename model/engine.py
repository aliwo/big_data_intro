import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# engine = create_engine(os.environ.get('SW_DATABASE_URI'), pool_recycle=300)
engine = create_engine('mysql+pymysql://root:22380476@localhost/SW?charset=UTF8MB4', pool_recycle=300)
SessionMaker = sessionmaker(bind=engine)



