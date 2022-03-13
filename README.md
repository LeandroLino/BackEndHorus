# BackEndHorus

# Tutorial de instalação Back-End

Após finizalizar o clone do repositório, você ir para a instalação total do projeto.

1 - Crie um ambiente virtual dentro do projeto com:
  ```python3 -m venv venv```
  
  
2 - Declare que irá utilizar esse ambiente com:
  ```source venv/bin/active```
  
  
3 - Agora dentro do ambiente será necessário instalar as dependecias, você pode fazer isso utilizando este comando:
  ```pip install -r requirements.txt```
  
  
4 - Agora basta rodar o projeto
  ```python manage.py runserver```
  Antes disso pode ser necessário criar todas as tabelas
  ```python manage.py migrate --run-syncdb``` 
  

# Documentação de endPoints

## POST /api/create/ - Adicionando um contato:

```
{
 "name":STRING,
 "telephone": STRING,
 "ddd": STRING
 }
```
**RESPONSE STATUS -> HTTP 201 - CREATED**
```
{
	"id": INT,
	"name": STRING,
	"telephone": STRING,
	"ddd": STRING
}
```

## PUT /api/edit/:id - Atualizando um contato:

```
{
 "name":STRING,
 "telephone": STRING,
 "ddd": STRING
 }
```
**RESPONSE STATUS -> HTTP 202 - Accepted**
```
{
	"name": STRING,
	"telephone": STRING,
	"ddd": STRING
}
```

## DELETE /api/delete/:id - Deletando um contato:

```
No Body
```
**RESPONSE STATUS -> HTTP 200 - Ok**
```
{}
```

## GET /api/edit/:id - Listando todos os contatos:

```
No Body
```
**RESPONSE STATUS -> HTTP 200 - Ok**
```
[{CONTACT}, {CONTACT}]
```
