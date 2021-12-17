import os
from enum import Enum
from pathlib import Path

from pydantic import BaseModel


class Env(str, Enum):
    LOCAL = "local"
    DEV = "dev"
    PREPROD = "preprod"
    PROD = "prod"


class Config(BaseModel):
    service_name: str
    broker: str
    backend: str
    queue: str
    version: str
    log_dir_path: Path
    log_level: str
    env: Env
    slack_bot_token: str


def init_config() -> Config:
    """
    Метод для инициализации параметров сервиса
    :return: Config, экземпляр класса с параметрами
    """
    # название сервиса, нужно указать свое при использовании шаблона
    service_name: str = os.getenv('SERVICE_NAME', 'slack_messenger_service')
    # параметры подключения к rabbitmq
    rabbit_user: str = os.getenv('RABBITMQ_DEFAULT_USER')
    rabbit_pass: str = os.getenv('RABBITMQ_DEFAULT_PASS')
    rabbit_host: str = os.getenv('RABBITMQ_DEFAULT_HOST', 'rabbitmq')
    rabbit_port: int = int(os.getenv('RABBITMQ_DEFAULT_PORT', 5672))
    queue = os.getenv("QUEUE", "slack_messenger_service.tasks")

    # параметры подключения к redis
    redis_host: str = os.getenv('REDIS_HOST', 'redis')
    redis_port: int = int(os.getenv('REDIS_PORT', 6379))

    broker: str = f"pyamqp://{rabbit_user}:{rabbit_pass}@{rabbit_host}:{rabbit_port}"
    backend: str = f"redis://{redis_host}:{redis_port}"
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    slack_bot_token = os.getenv("SLACK_BOT_TOKEN")

    return Config(
        service_name=service_name,
        broker=broker,
        backend=backend,
        version=os.getenv("VERSION", "0.0.0"),
        log_dir_path=os.getenv('LOG_DIR', f"/var/log/{service_name}/"),
        log_level=log_level,
        queue=queue,
        slack_bot_token=slack_bot_token,
        env=Env(os.getenv("ENV", Env.LOCAL))
    )


service_config = init_config()
