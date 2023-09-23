# Khanto API rest - Seazone

## Descrição do projeto 📄:

Desafio técnico lançado pela Seazone para a vaga de desenvolvedor full stack python. O projeto consiste em 3 API's REST, os quais apresentam endpoints para imóveis, anúncios e reservas.

## Tecnologias utilizadas 🧑‍💻:

+ Python
+ Django e Django REST framework
+ Docker
+ Pytest
+ Swagger

***

## Executando o projeto 🚀

#### 1. Clone o projeto do repositório no github e acesse o diretório baixado

        $ git clone https://github.com/brunosp1024/khanto-properties.git
        $ cd khanto-properties/


#### 2. Instale o Docker e o docker-compose seguindo as instruções na documentação

 - https://docs.docker.com/get-docker/


#### 3. Rodar docker-compose para iniciar o sistema

```shell script
docker-compose up
```

Esse comando executa as seguintes ações:
- Cria e inicia os containers;
- Aplica as migrações;
- Carrega dados predefinidos no banco de dados;
- Inicia o servidor;


#### 4. Defina uma nova senha para a variável SECRET_KEY no arquivo `.env` gerado. Isso aumeta aumeta a segurança do projeto:

    SECRET_KEY=exemploi3du7_6q39ydd0!ov$^tn%


#### 5. Criar um super usuário para acessar os endpoints do sistema

```shell script
docker-compose exec api python manage.py createsuperuser
```

***

## Acessando todos os endpoints 📌

Requisições para as API's:
| Método | Descrição |
|---|---|
| `GET` | Retorna um ou todos os itens. |
| `POST` | Cria um novo registro. |
| `PUT`/`PATCH` | Atualiza dados de um item. |
| `DELETE` | Remove um item do sistema. |

Estatus de respostas das API's
| Código | Descrição |
|---|---|
| `200` | Requisição executada com sucesso (success).|
| `201` | Recurso criado com sucesso (success).|
| `400` | Erros de validação ou os campos informados não existem no sistema.|
| `401` | Dados de acesso inválidos.|
| `404` | Recurso não encontrado (Not found).|

+ Requisição (application/json)

    + Authorization
 
        + username: "my_user"
        + password: 'minha_senha"


### Documentação das API's com swagger

No swagger é possível visualizar e acessar toda a documentação dos endpoints.
Endereço url para o swagger: http://localhost:8000/api/v1/swagger/

Para saber mais sobre essa ferramenta e seu funcionamento, acessar o link: https://www.youtube.com/watch?v=3nl9AzttzBQ

