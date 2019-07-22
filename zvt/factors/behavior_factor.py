# -*- coding: utf-8 -*-
from typing import List, Union

import pandas as pd

from zvt.domain import EntityType, ManagerTrading, Provider, IntervalLevel
from zvt.factors.factor import FilterFactor


class ManagerGiveUpFactor(FilterFactor):
    def __init__(self,
                 security_list: List[str] = None,
                 entity_type: Union[str, EntityType] = EntityType.stock,
                 exchanges: List[str] = ['sh', 'sz'],
                 codes: List[str] = None,
                 the_timestamp: Union[str, pd.Timestamp] = None,
                 start_timestamp: Union[str, pd.Timestamp] = None,
                 end_timestamp: Union[str, pd.Timestamp] = None,
                 columns=[ManagerTrading.volume],
                 filters: List = [ManagerTrading.trading_way == '减持'],
                 provider: Union[str, Provider] = 'eastmoney',
                 level: IntervalLevel = IntervalLevel.LEVEL_1DAY,
                 real_time: bool = False, refresh_interval: int = 10,
                 category_field: str = 'entity_id',
                 keep_all_timestamp: bool = True,
                 fill_method: str = 'ffill',
                 effective_number: int = 10) -> None:
        super().__init__(ManagerTrading, security_list, entity_type, exchanges, codes, the_timestamp, start_timestamp,
                         end_timestamp, columns, filters, provider, level, real_time, refresh_interval, category_field,
                         keep_all_timestamp, fill_method, effective_number)

    def compute(self):
        self.df = self.data_df.copy()
        self.df['score'] = False
        print(self.df)
        self.fill_gap()
        print(self.df)


if __name__ == '__main__':
    factor = ManagerGiveUpFactor(start_timestamp='2017-01-01', end_timestamp='2019-06-30')
    factor.compute()

    print(factor.df)
