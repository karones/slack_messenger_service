# Slack messenger


### Описание

Celery-сервис для отправки сообщений в Slack


## используемые переменные окружения

```
VERSION=1.0.0 // версия сервиса
RABBITMQ_DEFAULT_USER=admin // учетная запись для доступа к сервису rabbitmq 
RABBITMQ_DEFAULT_PASS=11111 // пароль к учетной записи для доступа к сервису rabbitmq
RABBITMQ_DEFAULT_PORT=5672 // порт по которому доступен сервис rabbitmq
RABBITMQ_DEFAULT_HOST=172.16.0.1 // хост по которому доступен сервис rabbitmq
QUEUE=slack_messenger_service.tasks // Название очереди
REDIS_HOST=172.17.0.1  // хост по которому доступен сервис redis
REDIS_PORT=6379 // порт по которому доступен сервис redis
CONCURRENCY=2 // Количество параллельных рабочих процессов
SLACK_BOT_TOKEN // Токен slack бота
```

## пример отправки задачи на отправку сообщения
```py
celery.send_task(
    "slack_messenger_service.send_message",
    queue='slack_messenger_service.tasks',
    args=(msg_channel, msg_text)
)
```

## пример запроса на отправку сообщения
```py
curl -X POST http://url:8000/api/v1/tasks/ \
-H 'Content-Type: application/json' \
-d '{
"task_name": "slack_messenger_service.send_message",
"task_args": {
"text": "test message",
"channel": "11111" // id канала 
}}'

пример ответа сервиса:

{"status":"ok","data":{"task_id":"3319bfbc-7af7-402d-80a6-e404db2d3ff4"},"debug":null,"error":null}
```
