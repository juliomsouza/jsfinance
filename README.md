#  JS Finance
O seu sistema de gestão financeira.

## Funcionalidades

O _JS Finance_ tem tudo o que você precisa para manter seu dinheiro no bolso.

Se maravilhe com esses recursos sensacionais de última geração:

- Contas a pagar;
- Contas a receber;

## Como contribuir

- Clone o repositório.

`git clone https://github.com/juliomsouza/jsfinance.git`

- Crie um virtualenv.

```
cd jsfinance
python -m venv .venv
source .venv/bin/activate
```

- Crie um virtualenv (WINDOWS).

```
cd jsfinance
virtualenv .venv
.venv/Scripts/activate
```

- Instale as dependências.

`pip install -r requirements.txt`

- Crie o banco MySQL.

```
mysql -e 'create database JSFINANCE;'
```

- Crie as tabelas do banco.

```
mysql -e 'source contrib/schema.sql;' JSFINANCE
```

- Popule o banco com dados de exemplo:

```
mysql -e 'source contrib/sample-data.sql;' JSFINANCE
```

ou se preferir utilize o [Docker](docker/README.md) para subir a base de dados.

- Crie um arquivo .env com a url de conexão do banco.

```
cat <<EOT >> .env
DATABASE_URL=mysql://root@127.0.0.1:3306/JSFINANCE
HELPDESK_URL=http://stackoverflow.com/
EOT
```

- Rode o programa:

`python -m jsfinance`

## Autor

- Julio M. Souza

## Colaboradores

- Henrique Bastos

## Licença

GPL 2.0
