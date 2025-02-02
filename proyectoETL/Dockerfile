FROM python:latest

WORKDIR /proyectoETL

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY . .

VOLUME "./proyectoETL/source/feed.xml"
VOLUME "./proyectoETL/target/"

#EXPOSE 8000

CMD [ "python", "main.py" ]
