# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Float

from zvt.domain.common import MacroBase, BaseMixin


class GDP(MacroBase, BaseMixin):
    __tablename__ = 'gdp'

    provider = Column(String(length=32))
    code = Column(String(length=32))
    name = Column(String(length=32))

    value = Column(Float)


class StockSummary(MacroBase, BaseMixin):
    __tablename__ = 'stock_summary'

    provider = Column(String(length=32))
    code = Column(String(length=32))
    name = Column(String(length=32))

    total_value = Column(Float)
    total_tradable_vaule = Column(Float)
    pe = Column(Float)
    volume = Column(Float)
    turnover = Column(Float)
    turnover_rate = Column(Float)
