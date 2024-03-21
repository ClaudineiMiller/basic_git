import os
from colorama import Fore, Style



def obter_tamanho_terminal():
    tamanho_terminal = os.get_terminal_size()
    linhas, colunas = tamanho_terminal.lines, tamanho_terminal.columns
    return linhas, colunas

def arrow():
    return color('—>', Fore.YELLOW)

def input_caracter(caracter, sub):
    return (obter_tamanho_terminal()[1] - sub) * caracter

def check_file_git():
    return True if os.path.exists(".git") else False

def check_file_path():
    return True if os.path.exists(".path.txt") else False


def color(texto, cor, estilo=Style.NORMAL):
    return f"{cor}{estilo}{texto}{Style.RESET_ALL}"

def clear():
    os.system('clear')

def get_user_input():
    userInput = input(f'\t{arrow()}  ')
    return userInput
    clear()


def main_title():
    clear()
    print(color(f'  {input_caracter("—", 2)}', Fore.GREEN))
    print(color(f'  |{"BASIC GIT".center(obter_tamanho_terminal()[1] -4)}|', Fore.GREEN))
    print(color(f'  {input_caracter("—", 2)}', Fore.GREEN))

def validar_entrada(entrada):
    tamanho = len(entrada)
    while True:
        entrada = input(f"Escolha um número de 1 a {tamanho}: ")
        if entrada.isdigit():  # Verifica se a entrada é composta apenas de dígitos
            numero = int(entrada)
            if 1 <= numero <= tamanho:  # Verifica se o número está dentro do intervalo válido
                return numero
            else:
                print(f"Erro: O número deve estar no intervalo de 1 a {tamanho}.")
        else:
            print("Erro: Por favor, digite um número inteiro válido.")









def title():
    clear()
    print(color('--------------------------------------------------------------------', Fore.GREEN))
    print(color('|   SISTEMA SIMPLIFICADO DE ENVIO DE ARQUIVOS PARA O GITHUB        |', Fore.GREEN))
    print(color('|------------------------------------------------------------------|', Fore.GREEN))
    print(color('| 1) Você precisa estar logado em sua conta do git para            |', Fore.YELLOW))
    print(color('|    que os comandos funcionem. Use os comandos abaixo:            |', Fore.YELLOW))
    print(color('|    git config --global user.name "Nome Completo"                 |', Fore.YELLOW))
    print(color('|    git config --global user.email "seuemail@exemplo.com"         |', Fore.YELLOW))
    print(color('| 2) Ou use a configuração com token com o comando:                |', Fore.YELLOW))
    print(color('|    git config --global credential.helper cache                   |', Fore.YELLOW))
    print(color('| 3) O comentário do "commit" no terminal deve estar entre aspas.  |', Fore.YELLOW))
    print(color('--------------------------------------------------------------------\n', Fore.GREEN))
