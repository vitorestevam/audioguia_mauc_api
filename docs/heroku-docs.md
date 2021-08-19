# Django rest framework + heroku 

Hospedar a aplicação no heroku é simples. o Aquivo heroku.yml vai ser o resposável pela configuração na plataforma.

``` yml

build:
  docker:
    web: dockerfile
run:
  web: python manage.py runserver 0.0.0.0:$PORT

```

Após isso, basta acessar o heroku e escolher a forma de enviar os arquivos para lá. No caso dessa aplicação eu preferi criar uma branch [Deploy](https://github.com/VitorEstevam/audioguia_mauc_api/tree/deploy) para guardar os arquivos que são enviados para lá e linkei o repositório ao Heroku.

![print heroku](./screenshot3.jpg)

## Referências

- https://devcenter.heroku.com/articles/build-docker-images-heroku-yml
- https://help.heroku.com/PPBPA231/how-do-i-use-the-port-environment-variable-in-container-based-apps