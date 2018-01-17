# Fase 3 - Análise de tráfego de rede

Acessando o link tinhamos acesso ao arquivo undeadsec.pcap

Arquivos pcap são criados a partir de um sniffer de rede, como tcpdump ou wireshark, e contém informações sobre os pacotes que trafegaram no adaptador sniffado.

Algumas estratégias utilizadas para análise do pcap:

### Foremost
Foremost é uma ferramenta de análise forense, permite recuperar arquivos deletados do disco rígido ou recuperar arquivos inseridos dentro de binários, por exemplo.

Aqui utilizaremos o foremost para extrair e reconstruir arquivos trafegados pela rede, como imagens, binários, etc.

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%203/Selection_052.png)

Porém o resultado disso não foi muito satisfatório, foi possível reconstruir alguns pedaçõs de imagens, além de alguns ícones e htmls de uma página apache genérica. Passamos para análise do pcap com o wireshark

### Wireshark
Com o wireshark, que também serve para siniffar a rede, abri o arquivo e procurei por alguma pista para a próxima fase.

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

## Fase 4
https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/tree/master/Fase%204
