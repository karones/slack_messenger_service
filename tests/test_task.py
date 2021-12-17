from celery import Celery
from celery.result import allow_join_result

from app.config import service_config

test_celery = Celery(service_config.service_name,
                     broker=service_config.broker,
                     backend=service_config.backend,
                     result_serializer='pickle',
                     accept_content=['pickle', 'json']
                     )


def test_run_task():
    msg_channel = 'C02EYS7TYEP'
    msg_text = '''Битые пути в company/770-plug
/goAnsOperator/Ans_NoWayToPlug  ========> file: company_770-plug/src/SPEC/Services/_goAnsServices.sc
-----------
WARNING:
/comMod_BullsAndCowsGame/BullsAndCows  ========> file: company_770-plug_dep/common/src/COMMON/_goAnsGames.sc
/comMod_KtoZhivetGame/StartGame  ========> file: company_770-plug_dep/common/src/COMMON/_goAnsGames.sc'''

    async_result = test_celery.send_task(
        f"{service_config.service_name}.send_message",
        queue=service_config.queue,
        args=(msg_channel, msg_text)
    )
    print(async_result.result)
    with allow_join_result():
        result = async_result.get()

    print(result)
    assert isinstance(result, dict)
