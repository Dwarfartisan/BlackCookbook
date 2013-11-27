#!/usr/bin/env python

import sqlalchemy as sa

engine = sa.create_engine("sqlite:///:memory:", echo=True)
print engine.table_names()

