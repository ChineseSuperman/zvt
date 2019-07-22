# -*- coding: utf-8 -*-
from typing import List, Union

import pandas as pd

from zvt.domain.common import EntityType, Provider, IntervalLevel
from zvt.trader.trader import Trader


class CoinTrader(Trader):
    entity_type = EntityType.coin

    def __init__(self,
                 security_list: List[str] = None,
                 exchanges: List[str] = ['huobipro'],
                 codes: List[str] = None,
                 start_timestamp: Union[str, pd.Timestamp] = None,
                 end_timestamp: Union[str, pd.Timestamp] = None,
                 provider: Union[str, Provider] = Provider.CCXT,
                 level: Union[str, IntervalLevel] = IntervalLevel.LEVEL_1DAY,
                 trader_name: str = None,
                 real_time: bool = False,
                 kdata_use_begin_time: bool = True) -> None:
        super().__init__(security_list, exchanges, codes, start_timestamp, end_timestamp, provider, level, trader_name,
                         real_time, kdata_use_begin_time)


class StockTrader(Trader):
    entity_type = EntityType.stock

    def __init__(self, security_list: List[str] = None,
                 exchanges: List[str] = ['sh', 'sz'],
                 codes: List[str] = None,
                 start_timestamp: Union[str, pd.Timestamp] = None,
                 end_timestamp: Union[str, pd.Timestamp] = None,
                 provider: Union[str, Provider] = Provider.JOINQUANT,
                 level: Union[str, IntervalLevel] = IntervalLevel.LEVEL_1DAY,
                 trader_name: str = None,
                 real_time: bool = False,
                 kdata_use_begin_time: bool = False) -> None:
        super().__init__(security_list, exchanges, codes, start_timestamp, end_timestamp, provider, level, trader_name,
                         real_time, kdata_use_begin_time)
