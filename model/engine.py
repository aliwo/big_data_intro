import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(os.environ.get('SW_DATABASE_URI'), pool_recycle=300)
SessionMaker = sessionmaker(bind=engine)



