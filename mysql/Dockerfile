FROM mysql:latest


# Establezca el directorio de trabajo en /app
WORKDIR /proyecto_etl/mysql

ADD . /proyecto_etl/mysql

# Establezca el usuario predeterminado para la imagen MySQL
USER mysql 

# Establezca las variables de entorno para el nuevo usuario
ENV MYSQL_USER=external_user 
ENV MYSQL_PASSWORD=password 
ENV MYSQL_DATABASE=my_database 

# Ejecute los siguientes comandos para crear el nuevo usuario y otorgarle los permisos necesarios
RUN mysql -u root -p -e "CREATE USER ' $MYSQL_USER '@'%' IDENTIFIED BY ' $MYSQL_PASSWORD ';"
RUN mysql -u root -p -e "GRANT ALL PRIVILEGES ON $MYSQL_DATABASE .* TO ' $MYSQL_USER '@'%';"
RUN mysql -u root -p -e "FLUSH PRIVILEGES;" 

# Exponer el puerto 3306 para permitir conexiones a la base de datos
EXPONER 3306 

# Iniciar el servidor MySQL cuando se ejecuta el contenedor
CMD [ "mysqld" ]