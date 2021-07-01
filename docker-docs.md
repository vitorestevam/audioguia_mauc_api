
# Django Rest framework + Docker

Para facilitar os testes e o futuro deploy da aplicação, decidimos testar o uso de docker.

## O que é docker?

Docker é um serviço para criar containers de aplicações. Com isso, as dependencias ficam especificadas em um aquivo e uma máquina virtual será criada para rodar nossa aplicação.

## Por que usar docker?

Com a Api em mãos percebemos que poderiamos passar pro problemas de hospedagem e de compartilhamento desse projeto entre diferentes máquinas por conta das dependências. A partir disso surgiu a Proposta de usar um container.

## Como rodar

Baixe e instale o docker

https://www.docker.com/get-started

No diretório do projeto rode o comando

```bash
  docker-compose up
```

A aplicação rodará na porta 8000

  
## Como funciona?

temos basicamente 2 arquivos fazendo a mágica:

#### dockerfile

Nele importamos as imagens e escrevemos comandos que vamos usar na nossa máquina virtual. 

o comando ``` ADD . /code/ ``` clona os arquivos para dentro da nossa máquina virtual.

#### docker-compose.yml

aqui nós configuramos como a aplicação vai rodar. No nosso caso, nós escrevemos o comando que o compose rodará quando subirmos a máquina e ligamos a porta 8000 do container à porta 8000 da nossa máquina.

  
## Referências

 - [Conteinerizando suas aplicações django com docker e docker-compose](https://medium.com/code-rocket-blog/conteinerizando-suas-aplica%C3%A7%C3%B5es-django-com-docker-e-docker-compose-3e86a8df6984)
 - [Semana do Flutter | RxNotifier Ep 2.1 - Trabalhando com Docker](https://www.youtube.com/watch?v=Hu_zm6VWlMU)
 - [Docker em 22 minutos - teoria e prática (Rápido!)](https://www.youtube.com/watch?v=Kzcz-EVKBEQ)

  
