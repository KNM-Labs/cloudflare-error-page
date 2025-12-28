# SPDX-License-Identifier: MIT

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    JSON,
    String,
    func,
)

from . import db


class Item(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(255), unique=True, nullable=False, index=True)
    params = Column(JSON, nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
