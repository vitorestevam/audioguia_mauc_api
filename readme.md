
# API AUDIO GUIA MAUC

REST API feita com [Django rest framework](https://www.django-rest-framework.org/) para ser usado na construção do app audio guia do Museu de Arte da Universidade Federal do Ceará.

## Onboarding

Antes de começar, dê uma olhada no [onboarding](/on_boarding.md) para entender como começar a trabalhar nos repositórios.

## Como rodar localmente
  
Instala o [Python](https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe) 
  
```
  Siga as instruções do instalador
```

Clona o projeto

```bash
  git clone https://link-to-project
```

Acessa o diretório do projeto

```bash
  cd maucproject
```

Instala as dependências

```bash
  pip install -r ./requirements.txt
```

Roda a aplicação

```bash
  python manage.py runserver
```

Veja a saída

``` bash
System check identified no issues (0 silenced).
September 08, 2022 - 22:22:52
Django version 3.2.15, using settings 'maucproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

vá para http://127.0.0.1:8000/admin (use a url que a saída acima mostrar)

Entre com o super user padrão com o usuário e senha  ```admin```, ```admin```

## Como criar um super user

Para acessar o dashboard e gerenciar o Guides você precisa criar um superuser
```
  python manage.py createsuperuser
```

Por padrão você pode usar ```admin```, ```admin``` nos primeiros acessos. Recomendo criar um novo e apagar o padrão.

https://docs.djangoproject.com/en/1.8/intro/tutorial02/

## Como hospedadar no Heroku (Heroku não possui mais plano free)

acesse o [heroku-docs.md](./docs/heroku-docs.md) para informações detalhadas

## API Reference

### Página de admin
```
  Acesse /admin

  user: admin
  password: admin
```

### Documentação dos endpoints pelo postman
  https://documenter.getpostman.com/view/15025870/TzmChYvb

<details>
  <summary>documentação detalhada dos endpoints</summary>
### Get all guides

```http
  GET /api/guides
```

Recebe uma lista de Guides

### Get guide

```http
  GET /api/guides/id
```

| field | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | a id do item |
| `name`      | `string` | nome da obra|
| `author`      | `string` | nome do autor|
| `alt_description`      | `string` | descrição textual da obra|
| `audio_description`      | `file` | audio descrição da obra|

Recebe um guide
  
</details>

## Referências

 - [Como criar uma API com django rest framework I](https://medium.com/@marcosrabaioli/criando-uma-api-rest-utilizando-django-rest-framework-parte-1-55ac3e394fa)   
 - [Como criar uma API com django rest framework II](https://www.django-rest-framework.org/tutorial/quickstart/)
 - [Como criar um diretório static no projeto](https://stackoverflow.com/questions/62737136/saving-image-file-in-particular-directory-in-django-rest-framework)
 - [Como impedir Requests de escrita não autenticados](https://www.django-rest-framework.org/api-guide/permissions/)
 
## Screenshots
![get return](docs/screenshot1.jpg)
![Admin page](docs/screenshot2.jpg)


## Sugestões de melhoria

- Hospedar o banco de forma separada para evitar que os deploys quebrem os dados que tão salvos na pasta static
