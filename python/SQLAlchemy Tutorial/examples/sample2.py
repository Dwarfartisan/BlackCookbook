#!/usr/bin/env python
# coding:utf-8

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import datetime

engine = sa.create_engine("sqlite:///:memory:", echo=True)
Base  = declarative_base()

class Note(Base):
    __tablename__ = 'note'
    id = sa.Column(sa.Integer, primary_key=True)
    author = sa.Column(sa.String)
    content = sa.Column(sa.String)
    at = sa.Column(sa.TIMESTAMP, default=datetime.datetime.now)

    def __repr__(self):
        return (u"<Note(id=%s, author='%s', content='%s', at='%s')>"%(
            self.id, self.author, self.content, self.at)).encode("utf-8")

Base.metadata.create_all(engine)

log = Note(author="mars.liu@tratao.com", content=u"编写 SQLAlchemy 教程")

Session = sessionmaker(bind=engine)
session = Session()
print log
session.add(log)
session.commit()
print log
