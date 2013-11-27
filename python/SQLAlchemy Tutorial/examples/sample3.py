#!/usr/bin/env python
# coding:utf-8

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import datetime
import pprint

engine = sa.create_engine("sqlite:///:memory:", echo=True)
Base  = declarative_base()

class Note(Base):
    __tablename__ = 'note'
    id = sa.Column(sa.Integer, primary_key=True)
    author = sa.Column(sa.String)
    content = sa.Column(sa.String, default="")
    at = sa.Column(sa.TIMESTAMP, default=datetime.datetime.now)

    def __repr__(self):
        return (u"<Note(id=%s, author='%s', content='%s...', at='%s')>"%(
            self.id, self.author, self.content[:5], self.at)).encode("utf-8")

Base.metadata.create_all(engine)

log = Note(author="mars.liu@tratao.com", content=u"SQLAlchemy 简介")

Session = sessionmaker(bind=engine)
session = Session()
session.add(log)
session.commit()

log1 = Note(author="mars.liu@tratao.com", content=u"SQLAlchemy 的查询语句")
log2 = Note(author="mars.liu@dwarf-artisan.com", content=u"SQLAlchemy 结构")

session.add_all([log1, log2])
session.commit()

re = session.query(Note).filter_by(author="mars.liu@tratao.com").all()
pprint.pprint(re)

re = session.query(Note.author, Note.at).all()
pprint.pprint(re)

log3 = Note(author="mars.liu@tratao.com", content=u"SQLAlchemy 增删改")
log3=session.merge(log3)
session.commit()
print log3
log3.author="march.liu@gmail.com"
log3=session.merge(log3)
session.commit()

re = session.query(Note.author, Note.at).all()
pprint.pprint(re)

log3 = session.query(Note).get(log3.id)
log3.author = "mars.liu@dwarf-artisan.com"
log3.content += u"，对象更新"
session.commit()
re = session.query(Note.author, Note.content).all()
pprint.pprint(re)

