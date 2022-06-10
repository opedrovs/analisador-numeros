from analisador.dados.menu import *
from analisador.dados.ferramentas import *

valores = []

menu()
while True:
    valor = leiaInt('Adicionar número (entre 1 e 100): ')
    if valor not in valores:
        valores.append(valor)
        print(f'{verde}Valor {amarelo}{valor} {verde}adicionado com sucesso!{limpar}')
    else:
        print(f'{vermelho}Valor {amarelo}{valor} {vermelho}já foi encontrado na lista!{limpar}')

    while True:
        resp = str(input(f'Quer continuar? [{verde}S{limpar}/{vermelho}N{limpar}] ')).strip().upper()
        if resp == 'S' or resp == 'N':
            break
        print(f'{vermelho}ERRO: Responda apenas S ou N.{limpar}')
    if resp == 'N':
        linha()
        break

menuOpcoes(valores)
menuFinal()
