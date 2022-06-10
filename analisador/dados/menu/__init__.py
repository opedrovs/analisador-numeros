from analisador.dados.menu import *
from analisador.dados.ferramentas import *


def linha():
    print(f'{azul}-{limpar}' * 35)


def menu():
    linha()
    print(f'{amarelo}Analisador Números'.center(42))
    linha()


def menuOpcoes(valores):
    while True:
        print('Veja algumas opções:')
        print(f'''{amarelo}[ 1 ] {azul}Ver valores
{amarelo}[ 2 ] {azul}Ver lista
{amarelo}[ 3 ] {azul}Adicionar valores
{amarelo}[ 4 ] {azul}Sair do programa{limpar}''')
        opc = leiaOpc(f'>>> Sua opção: ')
        if opc == 1:
            verValores(valores)
        elif opc == 2:
            verListaValores(valores)
        elif opc == 3:
            adicionarValores(valores)
        elif opc == 4:
            break
        linha()


def verValoresMenu():
    linha()
    print(f'{amarelo}Ver Valores'.center(42))
    linha()


def verValores(valores):
    verValoresMenu()
    print(f'Ao todo, temos {amarelo}{len(valores)}{limpar} números cadastrados.')
    print(f'O maior valor informado foi {verde}{max(valores)}{limpar}.')
    print(f'O menor valor informado foi {vermelho}{min(valores)}{limpar}.')
    print(f'Somando todos os valores, temos {verde}{sum(valores)}{limpar}.')
    print(f'A média dos valores digitados é {azul}{sum(valores) / len(valores):.1f}{limpar}.')


def verListaValoresMenu():
    linha()
    print(f'{amarelo}Ver Lista'.center(42))
    linha()


def verListaValores(valores):
    verListaValoresMenu()
    cont = 0
    for v in valores:
        cont += 1
        print(f'{v:2}, ' if cont < len(valores) else f'{v:2}. ', end='')
        if cont / 10 == 1:
            print()
            cont = 0
    print()


def adicionarValoresMenu():
    linha()
    print(f'{amarelo}Adicionar Valores'.center(41))
    linha()


def adicionarValores(valores):
    adicionarValoresMenu()
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
            break


def menuFinal():
    linha()
    print(f'{azul}<<< {amarelo}Fim do Programa {azul}>>>{limpar}'.center(60))
    linha()
