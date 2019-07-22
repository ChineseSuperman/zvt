# 数字货币
from sqlalchemy import Column, String

from zvt.domain.common import CoinMetaBase, BaseMixin


class Coin(CoinMetaBase, BaseMixin):
    __tablename__ = 'coin'

    entity_type = Column(String(length=64))
    exchange = Column(String(length=32))
    code = Column(String(length=32))
    name = Column(String(length=32))
