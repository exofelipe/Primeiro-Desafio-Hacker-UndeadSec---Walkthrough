
# -*- coding: iso-8859-15 -*-
from os import system
from base64 import b64decode

def main():
    system('clear')
    senha = 'SW5zaXJhIGEgc2VuaGE6IA=='
    entrada = raw_input(b64decode(senha))
    if entrada == b64decode(senha).lower()[::-1].upper():
        print '\n[*] Bem vindo.\n'
        raw_input('Parab..ns Voc.. conseguiu! Envie a senha para @A1S0N no telegram :D\n ---> https://t.me/A1S0N')
    else:
        print '\n[!] Senha inv..lida.\n'   
        raw_input('Pressione ENTER para continuar...')

while True:
    main()
