#Fase V - Análise de binário

Ao acessar a url podiamos baixar um arquivo binário windows, nomeado Trinity.exe

![](https://github.com/exofelipe/Primeiro-Desafio-Hacker-UndeadSec---Walkthrough/raw/master/Fase%205/Selection_065.png)

Pelo ícone logo de cara podiamos reconhecer o binário como sendo o famoso putty.exe, porém ao olhar mais de perto podiamos perceber que o binário não era EXATAMENTE o putty.exe.

Como assim? O binário tinha sido alterado. É possível verificar isso comparando os hashes MD5 ou SHA256 do binário, mas o que me chamou a atenção foi o fato de que o binário não estava assinado, ou seja, a assinatura que garante a sua integridade tinha sido corrompida ou removida.

Podemos verificar, no linux, através da ferramenta osslsigncode com o comando "osslsigncode verify <nomedoarquivo>"

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
