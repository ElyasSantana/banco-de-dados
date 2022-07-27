# Derivando da imagem oficial do MySQL
# docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=RootPassword
# -e MYSQL_DATABASE=Backoffice -e MYSQL_USER=MainUser -e
# MYSQL_PASSWORD=MainPassword backoffice-db
FROM mysql:5.7.9
# Adicionando os scripts SQL para serem executados na criação do banco
COPY ./db/ /docker-entrypoint-initdb.d/
COPY readme.csv /dados