# -*- coding: utf-8 -*-
import logging
import time

from apscheduler.schedulers.background import BackgroundScheduler

from zvt.recorders.sina.meta.sina_china_stock_category_recorder import SinaChinaStockCategoryRecorder
from zvt.recorders.sina.money_flow.sina_index_money_flow_recorder import SinaIndexMoneyFlowRecorder
from zvt.utils.utils import init_process_log

logger = logging.getLogger(__name__)

sched = BackgroundScheduler()


@sched.scheduled_job('cron', hour=17, minute=00)
def run():
    while True:
        try:
            SinaChinaStockCategoryRecorder().run()

            SinaIndexMoneyFlowRecorder().run()
            break
        except Exception as e:
            logger.exception('sina runner error:{}'.format(e))
            time.sleep(60)


if __name__ == '__main__':
    init_process_log('sina_runner.log')

    run()

    sched.start()

    sched._thread.join()
