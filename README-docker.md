# Utilização do Docker para subir base de dados

## Dependências
* [docker](https://download.docker.com/)
* [docker-compose](https://pypi.org/project/docker-compose/)

## Provisionar ambiente

1. Copie o arquivo `contrib/.env` para a raiz do projeto ou crie um com as variáveis definidas no arquivo de exemplo.

2. Execute:

```bash
docker-compose up -d
```

> para testar execute:

```bash
source .env

docker-compose exec mysql mysql -u $MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DATABASE
```
Para que os dados do banco de desenvolvimento não sejam perdidos descomente a **linha 14** do arquivo docker-compose.yml e crie um diretório **data** na raiz do projeto.
