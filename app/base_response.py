from enum import Enum
from typing import Optional, Any, Union, Dict

from pydantic import BaseModel


class Status(str, Enum):
    STATUS_OK = "ok"
    STATUS_ERROR = "error"

    def __str__(self):
        """
        метод для получения строкового литерала статуса
        :return:
        """
        return self.value


class BaseResponse(BaseModel):
    """
    Базовая структура ответа сервиса.
    Все структуры ответов должны наследоваться от этого класса и переопределять параметр data.
    status - всегда либо ok, либо error
    data - полезная нагрузка, переопределяется структурой самой ручки
    error - слаг ошибки, крайне рекомендуется не отдавать сырой ответ
    debug - структура (или строка) для более подробного описания ошибки
    """

    status: Status
    data: Optional[str]
    debug: Optional[str]
    error: Optional[str]

    class Config:
        use_enum_values = True
