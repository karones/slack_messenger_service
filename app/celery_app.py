from celery import Celery

from config import service_config as config


celery = Celery(config.service_name,
                broker=config.broker,
                backend=config.backend,
                result_serializer='pickle',
                accept_content=['pickle', 'json']
                )
