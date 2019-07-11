# Utilização do Docker para subir base de dados

## Dependências
* Docker
* Docker Compose

## Comandos

* Subir imagem
```docker
docker-compose up
```
* Criar a base de dados
```docker
docker-compose exec mariadb mysql -e 'create database JSFINANCE;'
```

* Criar estrutura de tabelas
```docker
docker-compose exec mariadb mysql -e 'source /contrib/schema.sql;' JSFINANCE
```

* Popular banco com dados de exemplo
```docker
docker-compose exec mariadb mysql -e 'source /contrib/sample-data.sql;' JSFINANCE
```