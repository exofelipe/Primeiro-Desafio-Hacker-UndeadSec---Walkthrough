# Fase I - O Vídeo e SunTzu

A primeira parte do desafio se iniciou com o vídeo publicado no youtube (http://youtu.be/YpFD9Fxm6YU)

Algumas coisas chamaram atenção no vídeo, entre essas:

* 1  A página aberta no navegador 
![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%201/video1.png) 

* 2  O script python rodando no terminal 
![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%201/video2.png)

* 3  O código python impresso na mesa
![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%201/video3.png)

Resolvi investigar a página aberta, já que está poderia conter alguma pista para o próximo desafio. 
Trata-se da página hospedada no github da undeadsec, página que contém as regras do grupo @UndeadSec no telegram.
Observando os últimos comits ao projeto undeadsec.github.io podemos ver que houve, na mesma data do vídeo, um commit com o nome SunTzu, isso já comprovava minha suspeita de que a página teria algo a ver com o desafio. Observando o arquivo em questão, index.html, podemos encontrar o que estava buscando.

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%201/video5.png)

URL: http://github.com/WarTzu

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%201/commit%20github.png)


Acessando o link chegavamos a uma conta nomeada WarTzu, com apenas um projeto, https://github.com/WarTzu/.-

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%201/github2.png)

Esse projeto por sua vez possui apenas um arquivo zip com o nome SunS3cur2.zip, podemos baixar então esse arquivo e verificar que é necessária uma senha para descompactá-lo, vamos voltar ao vídeo.

Investigando o código impresso, podemos perceber que se trata do projeto EvilURL da UndeadSec (https://github.com/UndeadSec/EvilURL) mas o projeto em si não é a nossa pista, no vídeo é possível enchergar, em meio as linhas do código, algo que não pertence ao projeto:

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%201/video4.png)


p4ssw0rd: "Z0mB!3C0Wb0y&&*@"

Usando a senha no zip chegamos ao arquivo SunTzu.txt, que possui uma url tendo os caracteres espalhados linha a linha

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%201/link.png)

Dessa forma obtemos a url para a segunda parte, outro vídeo no youtube:
https://youtu.be/XFnPOTnwSDc

O script rodando no terminal, por sua vez, não faz parte do desafio.
