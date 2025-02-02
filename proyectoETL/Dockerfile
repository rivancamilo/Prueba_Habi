FROM python:latest

WORKDIR /proyectoETL

COPY requirements.txt requirements.txt
RUN pip install --upgrade mysql-connector-python
RUN pip install virtualenv
#RUN pip install requests SQLAlchemy pandas pymysql mysql-connector-python python-dotenv python-decouple
RUN pip install -r requirements.txt


RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

RUN curl -o wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x wait-for-it.sh

COPY . .

#CMD [ "python", "./main.py" ]
CMD ["sh", "-c", "./wait-for-it.sh mysql:3306 -- sleep 60 && python ./main.py"]
