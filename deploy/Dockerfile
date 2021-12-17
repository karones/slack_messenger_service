FROM python:3.8-slim

# set work directory
WORKDIR /opt/slack-messenger-service/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT 1
ENV PIP_INDEX_URL=https://artifactory.company.team/artifactory/api/pypi/common-pip-group/simple

# install dependencies
RUN --mount=type=secret,id=netrc,required=true,target=/root/.netrc \
    pip install --upgrade pip
COPY ./deploy/requirements.txt .
RUN --mount=type=secret,id=netrc,required=true,target=/root/.netrc \
    pip install -r requirements.txt

COPY app .

CMD celery -A tasks worker --loglevel=info -Q $QUEUE -c $CONCURRENCY
