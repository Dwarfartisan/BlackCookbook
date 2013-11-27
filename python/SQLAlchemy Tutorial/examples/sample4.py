#!/usr/bin/env python
# coding:utf-8

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import datetime
import pprint

engine = sa.create_engine("sqlite:///:memory:", echo=True)
Base  = declarative_base(bind=engine)

class Note(Base):
    __tablename__ = 'note'
    id = sa.Column(sa.Integer, primary_key=True)
    author = sa.Column(sa.String)
    content = sa.Column(sa.String, default="")
    at = sa.Column(sa.TIMESTAMP, default=datetime.datetime.now)

    def __repr__(self):
        return (u"<Note(id=%s, author='%s', content='%s...', at='%s')>"%(
            self.id, self.author, self.content[:25], self.at)).encode("utf-8")

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

log3 = Note(author="mars.liu@tratao.com", content=u"SQLAlchemy 增删改")
log3=session.merge(log3)
session.commit()
log3.author="march.liu@gmail.com"
log3=session.merge(log3)
session.commit()

ins = Note.__table__.insert().values(author='march.liu@gmail.com', content=u"SQL语句组合")
print ins

session.execute(ins)
re = session.query(Note).all()
print re 

log4 = session.query(Note).order_by(Note.id.desc()).first()
print log4
log4.content += u"，数据已修改成功"
session.commit()
re = session.query(Note.id, Note.content).all()
pprint.pprint(re)
print log4.content
