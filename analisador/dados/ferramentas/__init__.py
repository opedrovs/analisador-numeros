from analisador.decoracao.cores import *


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print(f'{vermelho}\nUsuário preferiu não digitar o valor!{limpar}')
            return 0
        except:
            print(f'{vermelho}ERRO: Digite um valor válido!{limpar}')
        else:
            if n < 1 or n > 100:
                print(f'{vermelho}ERRO: Aceitamos apenas valores entre 1 e 100.{limpar}')
            else:
                num = int(n)
                return num


def leiaOpc(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print(f'{vermelho}\nUsuário preferiu não digitar o valor!{limpar}')
            return 0
        except:
            print(f'{vermelho}ERRO: Digite um valor válido!{limpar}')
        else:
            if n >= 1 or n <= 4:
                num = int(n)
                return num
            else:
                print(f'{vermelho}ERRO: Opção inválida! Tente novamente!.{limpar}')
