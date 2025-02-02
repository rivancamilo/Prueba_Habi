FROM python:latest

WORKDIR /proyectoETL

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY . .

VOLUME "./etl/source/feed.xml"
VOLUME "./etl/target/"
VOLUME [ "/data" ]

#EXPOSE 8000

CMD [ "python", "main.py" ]
