from jqdatasdk import auth, query, finance

from zvdata.recorder import TimeSeriesDataRecorder
from zvdata.utils.utils import multiple_number
from zvt.domain import Index, CrossMarketSummary
from zvt.settings import JQ_ACCOUNT, JQ_PASSWD
from zvt.utils.time_utils import to_time_str


class StockSummaryRecorder(TimeSeriesDataRecorder):
    entity_provider = 'exchange'
    entity_schema = Index

    provider = 'joinquant'
    data_schema = CrossMarketSummary

    def __init__(self, batch_size=10,
                 force_update=False, sleeping_time=5, default_size=2000, one_shot=False,
                 fix_duplicate_way='add') -> None:

        # 聚宽编码
        # 市场通编码	市场通名称
        # 310001	沪股通
        # 310002	深股通
        # 310003	港股通（沪）
        # 310004	港股通（深）

        codes = ['310001', '310002', '310003', '310004']
        super().__init__('index', ['cn'], None, codes, batch_size,
                         force_update, sleeping_time,
                         default_size, one_shot, fix_duplicate_way)

        auth(JQ_ACCOUNT, JQ_PASSWD)

    def init_entities(self):
        super().init_entities()

    def record(self, entity, start, end, size, timestamps):

        q = query(finance.STK_ML_QUOTA).filter(
            finance.STK_ML_QUOTA.link_id == entity.code,
            finance.STK_ML_QUOTA.day >= to_time_str(start)).limit(2000)

        df = finance.run_query(q)
        print(df)

        json_results = []

        for item in df.to_dict(orient='records'):
            result = {
                'provider': self.provider,
                'timestamp': item['day'],
                'name': entity.name,
                'buy_amount': multiple_number(item['buy_amount'], 100000000),
                'buy_volume': item['buy_volume'],
                'sell_amount': multiple_number(item['sell_amount'], 100000000),
                'sell_volume': item['sell_volume'],
                'quota_daily': multiple_number(item['quota_daily'], 100000000),
                'quota_daily_balance': multiple_number(item['quota_daily_balance'], 100000000)
            }

            json_results.append(result)

        if len(json_results) < 100:
            self.one_shot = True

        return json_results

    def get_data_map(self):
        return None


if __name__ == '__main__':
    StockSummaryRecorder(batch_size=30).run()
