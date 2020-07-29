ARG INSTALL_PYTHON_VERSION=${INSTALL_PYTHON_VERSION:-3.8.2}
FROM python:${INSTALL_PYTHON_VERSION}-slim

ENV PYTHONDONTWRITEBYTECODE 1

RUN set -ex && \
    apt-get update && \
    apt-get -y install netcat && \
    apt-get clean

RUN mkdir /code
WORKDIR /code

COPY requirements requirements
RUN pip install --upgrade pip && \
    pip install -r requirements/dev.txt

COPY . .

EXPOSE 8000

CMD ["./entrypoint.sh"]
