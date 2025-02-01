FROM python:latest

COPY .  ./app

WORKDIR /app

#instalamos todas las librerias necesarias
RUN pip install mysql-connector-python pymysql pandas SQLAlchemy

VOLUME "/app/data"

CMD [ "python", "./main.py" ]
