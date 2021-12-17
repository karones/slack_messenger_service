from typing import Dict

from slack_sdk import WebClient

from base_response import BaseResponse, Status
from celery_app import celery
from config import service_config as config
from logger import logger

slack_client = WebClient(token=config.slack_bot_token)


@celery.task(name=f"{config.service_name}.send_message",
             queue=f"{config.queue}")
def send_message(channel: str, text: str) -> Dict[str, str]:
    """таск для отправки сообщений в slack

    Args:
        channel (str): ИД канала
        text (str): Текст сообщения
    """
    response = BaseResponse(
        status=Status.STATUS_OK,
        data="",
        debug="",
        error=""
    )
    logger.info(f"Start task with params channel={channel}, text={text}")

    try:
        slack_client.chat_postMessage(channel=channel, text=text)
    except Exception as e:
        response.status = Status.STATUS_ERROR
        response.error = type(e).__name__
        response.debug = str(e)

    logger.info("End execute task")

    logger.info(response.dict())

    return response.dict()
