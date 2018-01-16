Fase I - O Vídeo e o arquivo

A primeira parte do desafio se iniciou com o vídeo publicado no youtube (http://youtu.be/YpFD9Fxm6YU)

Algumas coisas chamaram atenção no vídeo, entre essas:
1: A página aberta no navegador [INSERIR IMAGEM 1]
2: O script python rodando no terminal [INSERIR IMAGEM 2]
3: O código python impresso na mesa [INSERIR IMAGEM 3]

Resolvi investigar a página aberta, já que está poderia conter alguma pista para o próximo desafio. 
Trata-se da página hospedada no github da undeadsec, página que contém as regras do grupo @UndeadSec no telegram.
Observando os últimos comits ao projeto undeadsec.github.io podemos ver que houve, na mesma data do vídeo, um commit com o nome SunTzu, isso já comprovava minha suspeita de que a página teria algo a ver com o desafio. Observando o arquivo em questão, index.html, podemos encontrar o que estava buscando.
[INSERIR IMAGEM 5]
URL: http://github.com/WarTzu

Acessando o link chegavamos a uma conta nomeada WarTzu, com apenas um projeto, https://github.com/WarTzu/.-
Esse projeto por sua vez possui apenas um arquivo zip com o nome SunS3cur2.zip, podemos baixar então esse arquivo e verificar que é necessária uma senha para descompactá-lo, vamos voltar ao vídeo.

Investigando o código impresso, podemos perceber que se trata do projeto EvilURL da UndeadSec (https://github.com/UndeadSec/EvilURL) mas o projeto em si não é a nossa pista, no vídeo é possível enchergar, em meio as linhas do código, algo que não pertence ao projeto:
[INSERIR IMAGEM 4]
p4ssw0rd: "Z0mB!3C0Wb0y&&*@"

Usando a senha no zip chegamos ao arquivo SunTzu.txt, que possui uma url tendo os caracteres espalhados linha a linha
[INSERIR IMAGEM 6]

Dessa forma obtemos a url para a segunda parte, outro vídeo no youtube:
https://youtu.be/XFnPOTnwSDc

O script rodando no terminal, por sua vez, não faz parte do desafio.
