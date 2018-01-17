# Parte IV - Cifra de Cesar e Steganografia I

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

## Fase 5
https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/tree/master/Fase%205
