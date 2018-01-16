Fase 6 - FINAL

A fase anterior nos levou a uma url na qual podíamos baixar um arquivo de áudio, thewall2.wav

Ao escutar o arquivo podiamos perceber que se tratava de um código morse (de novo), mas isso não é tudo.

Obtinhamos o seguinte texto:

O ESCOLHIDO - isso é uma dica que utilizaremos mais tarde

Além disso havia algo estranho no início do arquivo, um ruído diferente.

Abrindo o arquivo wav em um analisador espectral podiamos perceber o ruído em questão. Bem estranho considerando que o mesmo tipo de audio ja havia sido utilizado antes no desafio e não havia esse ruído.

Podiamos então supor que se trata de outro caso de steganografia, bastava descobrir qual a técnica e algoritmo utilizado para inserir o arquivo no som.

Em alguns minutos chegou a próxima dica

Um link para uma url no pastebin com um início de url que deveria ser utilizado bruteforce para completá-la.

https://goo.gl/wUt1y<BRUTE>

Com um simples python podemos testar todas as urls

Olhando uma a uma encontravamos nossa ferramenta:

http://jpinsoft.net/deepsound/

Definitivamente era a nossa pista.

Utilizando a ferramenta podiamos encontrar dois arquivos dentro do nosso audio

Porém para extraí-la era necessário uma senha. 

Lembram-se da string encontrada no início? pois então, não é ela.

É necessário o básico de conhecimento nerd para passar dessa etapa, já que os últimos passos tiveram referência ao Matrix a resposta não fica tão difícil, quem é "O escolhido" no filme? Neo. Essa sim é nossa senha.

Estamos perto do fim, os arquivos extraídos são dois arquivos texto.

O conteúdo dos arquivos parece bem ofuscado, e a uma primeira olhada reconhecemos o base64 (final ==) na chave (teoricamente não está errado, mas você não vai ir muito longe apenas com essa informação).

Prestando atenção no arquivo key.txt podemos perceber que é uma chave privada RSA, uma forma bem utilizada de criptografia assimétrica. 

Basta, então, decriptografarmos a strings.

Podemos fazer o decrypt com o openssl, por facilidade decidi usar uma ferramenta online.

E voilà, obtinhamos a flag final do nosso desafio.

"Você venceu o desafio! Aqui está sua chave de vitória:
h2he-12e-0210-9124-04=3240=23432edxUndead@@

Enviadas as chaves, está concluido o desafio.
