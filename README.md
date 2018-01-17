# Primeiro-Desafio-Hacker-UndeadSec---Walkthrough
Passo a passo para completar o desafio da UndeadSec publicado em 11 de janeiro de 2018

## Fase I - O Vídeo e SunTzu

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

Investigando o código impresso, podemos perceber que se trata do projeto EvilURL da UndeadSec (https://github.com/UndeadSec/EvilURL) mas o projeto em si não é a nossa pista, no vídeo é possível enxergar, em meio as linhas do código, algo que não pertence ao projeto:

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%201/video4.png)


p4ssw0rd: "Z0mB!3C0Wb0y&&*@"

Usando a senha no zip chegamos ao arquivo SunTzu.txt, que possui uma url tendo os caracteres espalhados linha a linha

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%201/link.png)

Dessa forma obtemos a url para a segunda parte, outro vídeo no youtube:
https://youtu.be/XFnPOTnwSDc

O script rodando no terminal, por sua vez, não faz parte do desafio.

## Fase 2 - Código morse e E-mail
https://www.youtube.com/watch?v=XFnPOTnwSDc

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%202/Selection_044.png)

Observando esse vídeo duas coisas chamam a atenção:

* Os escritos em chinês, provavelmente referências ao SunTzu e ao seu livro
* O áudio do vídeo, claramente em código morse

É possível interpretar código morse manualmente (trabalhoso) portanto utilizei uma ferramenta online para facilitar o trabalho (https://morsecode.scphillips.com/labs/decoder) 

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%202/Selection_045.png)


![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%202/Selection_046.png)

Mensagem: 
SUNTZUWAR.GITHUB.IO

Acessando o link podemos ter acesso a seguinte página:

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%202/Selection_047.png)

Utilizando o tradutor do google para obter a tradução para os escritos:

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%202/Selection_049.png)

Basta então pegarmos o e-mail do script e enviar uma mensagem. Porém é preciso ter atenção! O e-mail copiado da página não é válido, algumas letras estão representadas em unicode, e não são caracteres ascii, devemos então reescrever o endereço antes de enviar o e-mail

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%202/Selection_048.png)

bootrootwar@gmail.com

Após alguns minutos recebemos a nossa resposta com o link para a próxima fase

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%202/Selection_050.png)

https://goo.gl/Ek8Ehj

## Fase 3 - Análise de tráfego de rede

Acessando o link tinhamos acesso ao arquivo undeadsec.pcap

Arquivos pcap são criados a partir de um sniffer de rede, como tcpdump ou wireshark, e contém informações sobre os pacotes que trafegaram no adaptador sniffado.

Algumas estratégias utilizadas para análise do pcap:

### Foremost
Foremost é uma ferramenta de análise forense, permite recuperar arquivos deletados do disco rígido ou recuperar arquivos inseridos dentro de binários, por exemplo.

Aqui utilizaremos o foremost para extrair e reconstruir arquivos trafegados pela rede, como imagens, binários, etc.

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%203/Selection_052.png)

Porém o resultado disso não foi muito satisfatório, foi possível reconstruir alguns pedaçõs de imagens, além de alguns ícones e htmls de uma página apache genérica. Passamos para análise do pcap com o wireshark

### Wireshark
Com o wireshark abri o arquivo e procurei por alguma pista para a próxima fase.

Após filtrar as requisições http foi possível encontrar uma chamada GET baixando um script python. Encontramos nossa pista

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%203/Selection_053.png)

GET /final.py

Utilizando o wireshark para reconstruir a requisição HTTP podemos obter o script em questão:

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%203/Selection_054.png)

Trata-se de um script python que testa uma senha e pede para enviá-la para o telegram de @A1S0N.

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%203/Selection_055.png)

Basta executarmos o teste com o python para obtermos a senha 

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%203/Selection_056.png)

" :AHNES A ARISNI"

Podemos enviar então essa senha para o endereço do telegram

Em poucos minutos temos a pista para a próxima fase:

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%203/Selection_057.png)

https://goo.gl/dBHBJm

## Parte IV - Cifra de Cesar e Steganografia I

Ao acessar a url obtida no passo anterior, temos acesso à um arquivo ERROR.tar.xz, trata-se de um arquivo comprimido, podemos extrair facilmente com o linux

Após extrair nosso tar.xz temos três arquivos:
senha.txt
smith.zip
cipher.jpg

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%204/Selection_058.png)

O arquivo smith.zip é um arquivo compactado com senha, podemos supor então que o objetivo dos outros dois arquivos é entregar a senha para nosso compactado.

Abrindo o arquivo senha.txt temos o seguinte:

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%204/Selection_059.png)

Pelo parâmetro "shift" podemos perceber que a string da primeira linha está encriptada com uma cifra de cesar. Cifra de cesar é um algoritmo bem conhecido e bem simples na criptografia que se baseia em trocar cada letra da frase por outra da sequência do alfabeto, basta saber quantas casas ("shift") se tem que andar no alfabeto para descobrir a frase original.

Caso o desafiante não conhecesse sobre criptografia a imagem era uma dica, trata-se de uma estátua de Júlio Cesar, podia-se associar o nome do arquivo "cipher" com Cesar para descobrir o algoritmo utilizado.

Aplicando o reverso da cifra de cesar obtemos a senha original do arquivo:

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%204/Selection_060.png)

ReeVeslWaLls

Basta aplica-la em minúsculo em nosso arquivo compactado para abrí-lo

O compactado continha dentro dele apenas uma imagem, smith.jpg, sendo essa nossa pista para a próxima fase, podiamos supor que se trata de um desafio de steganografia.

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%204/Selection_061.png)

A steganografia se trata de um conjunto de várias técnicas que permitem esconder uma informação dentro de uma imagem, vídeo, som, entre outros.

Para solucionar esse tipo de desafio uma boa idéia é começar observando os metadados do arquivo, geralmente tem alguma pista sobre as modificações que foram feitas nele ou até mesmo a própria resposta para o desafio pode estar lá.

Para observar os metadados do arquivo utilizei o exiftool.

O output da ferramenta é o seguinte:

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%204/Selection_063.png)

Podemos observar algumas entradas estranhas, que não são parãmetros normais para os metadados:

* Image Description               : aHR0cHM6Ly9nb28uZ2wvR3VLSnNu
* Artist                          : VW5kZWFk
* Copyright                       : VW5kZWFkU2Vj
* Owner Name                      : VW5kZWFkU2Vj

Facilmente é possível perceber que tratam-se de strings encodadas em base64, utilizando o python podemos rapidamente decodar essas strings:

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%204/Selection_064.png)

E ai está nossa pista para a próxima fase.

https://goo.gl/GuKJsn

## Fase V - Análise de binário

Ao acessar a url podiamos baixar um arquivo binário windows, nomeado Trinity.exe

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%205/Selection_065.png)

Pelo ícone logo de cara podiamos reconhecer o binário como sendo o famoso putty.exe, porém ao olhar mais de perto podiamos perceber que o binário não era EXATAMENTE o putty.exe.

Como assim? O binário tinha sido alterado. É possível verificar isso comparando os hashes MD5 ou SHA256 do binário, mas o que me chamou a atenção foi o fato de que o binário não estava assinado, ou seja, a assinatura que garante a sua integridade tinha sido corrompida ou removida.

Podemos verificar, no linux, através da ferramenta osslsigncode com o comando "osslsigncode verify NOME_DO_ARQUIVO"

Output do putty original

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%205/Selection_067.png)

Output do Trinity.exe

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%205/Selection_066.png)

Portanto nossa próxima pista está dentro desse binário. Uma forma interessante de procurar modificações no binário, antes de utilizar engenharia reversa ou outras técnicas mais trabalhosas, é observar as strings contidas dentro dele

Como as outras fases sempre terminavam com url, supus que seria uma boa idéia começar buscando por elas

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%205/Selection_069.png)

BINGO! encontramos nossa próxima pista:

A_MATRIX_ESTA_EM_VOCE_https://goo.gl/tm7ojX

https://goo.gl/tm7ojX

## Fase 6 - FINAL

A fase anterior nos levou a uma url na qual podíamos baixar um arquivo de áudio, thewall2.wav

Ao escutar o arquivo podiamos perceber que se tratava de um código morse (de novo), mas isso não é tudo.

Obtinhamos o seguinte texto procedendo da mesma forma que anteriormente:

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%206/Selection_071.png)

O ESCOLHIDO - isso é uma dica que utilizaremos mais tarde

Além disso havia algo estranho no início do arquivo, um ruído diferente.

Abrindo o arquivo wav em um analisador espectral podiamos perceber o ruído em questão. Bem estranho considerando que o mesmo tipo de áudio ja havia sido utilizado antes no desafio e não havia esse ruído.

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%206/Selection_070.png)

Podiamos então supor que se trata de outro caso de steganografia, bastava descobrir qual a técnica e algoritmo utilizado para inserir o arquivo no som.

Em alguns minutos chegou a próxima dica.

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%206/Selection_072.png)

Um link para uma url no pastebin com um início de url que deveria ser utilizado bruteforce para completá-la.

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%206/Selection_073.png)

https://goo.gl/wUt1y< BRUTE>

Com um simples python podemos testar todas as urls

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%206/Selection_074.png)

Acessando uma a uma as urls possíveis, foi possível identificar a ferramenta que utiliza a técnica que estava buscando:

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%206/Selection_075.png)

http://jpinsoft.net/deepsound/

Definitivamente era a nossa pista.

Utilizando a ferramenta podiamos encontrar dois arquivos dentro do nosso audio

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%206/Selection_076.png)

Porém para extraí-la era necessário uma senha. 

Lembram-se da string encontrada no início? pois então, não é ela.

É necessário o básico de conhecimento nerd para passar dessa etapa, já que os últimos passos tiveram referência ao Matrix a resposta não fica tão difícil, quem é "O escolhido" no filme? Neo. Essa sim é nossa senha.

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%206/Selection_077.png)

Estamos perto do fim, os arquivos extraídos são dois arquivos texto.

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%206/Selection_078.png)

O conteúdo dos arquivos parece bem ofuscado, e a uma primeira olhada reconhecemos o base64 (final ==) na chave (teoricamente não está errado, mas você não vai ir muito longe apenas com essa informação).

Prestando atenção no arquivo key.txt podemos perceber que é uma chave privada RSA, uma forma bem utilizada de criptografia assimétrica. 

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%206/Selection_083.png)

Basta, então, decriptografarmos a strings.

Podemos fazer o decrypt com o openssl, por facilidade decidi usar uma ferramenta online.

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%206/Selection_084.png)

E voilà, obtinhamos a flag final do nosso desafio.

"Você venceu o desafio! Aqui está sua chave de vitória:
h2he-12e-0210-9124-04=3240=23432edxUndead@@

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%206/Selection_085.png)

Enviadas as chaves, está concluido o desafio.


# Agradecimentos 
* @A1S0N e a equipe do UndeadSec pela proposta do desafio
* @luucas-aps pelo apoio e revisão do tutorial
* @Todos que me ajudaram na construção do conhecimento necessário para realizar esse desafio e tantos outros a mais em minha vida


##### Two roads diverged in a wood, and I—. I took the one less traveled by. And that has made all the difference
###### Robert Frost - The Road Not Taken
