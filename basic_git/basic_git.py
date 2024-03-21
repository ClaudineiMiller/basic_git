import subprocess
import os
import shlex
from colorama import Fore, Style

def main():
    titulo()

    if not os.path.exists(".git"):
        print(colorir('-----------------------------------------------------------------', Fore.RED))
        print(colorir('| ERRO: ESTE PROGRAMA SÓ FUNCIONA DENTRO DE UM REPOSITÓRIO GIT. |', Fore.RED))
        print(colorir('| USE O COMANDO "git init" PARA CRIAR UM REPOSITÓRIO OU O       |', Fore.RED))
        print(colorir('| COMANDO "git clone" PARA CLONAR UM REPOSITÓRIO.               |', Fore.RED))
        print(colorir('-----------------------------------------------------------------', Fore.RED))
        return

    if not verificar_modificacoes_git():
        print(colorir('--------------------------------------------------------', Fore.WHITE))
        print(colorir("|  >>> NENHUM ARQUIVO MODIFICADO PARA SER ENVIADO. <<< |", Fore.RED))
        print(colorir('--------------------------------------------------------\n', Fore.WHITE))
        return

    commit_user = input(colorir('Escreva abaixo o comentário do commit:\n>>> ', Fore.YELLOW))
    titulo()

    commit = shlex.quote(commit_user)

    try:
        subprocess.run(["git", "add", "."], capture_output=True, check=True)
        print(colorir('> Comando enviado: "git add ."', Fore.CYAN))
        print(colorir('Todos os arquivos modificados foram adicionados.', Fore.CYAN))
    except subprocess.CalledProcessError as e:
        print(colorir(f"Erro ao adicionar arquivos: {e.stderr.decode('utf-8').strip()}", Fore.RED))
        return

    print(colorir('-----------------------------------------------------------\n', Fore.GREEN))

    try:
        subprocess.run(["git", "commit", "-a", "-m", commit], capture_output=True, check=True)
        print(colorir(f'> Comando enviado: "git commit -a -m {commit_user}"', Fore.CYAN))
        print(colorir('Um commit com a mensagem do usuário foi criado.', Fore.CYAN))
    except subprocess.CalledProcessError as e:
        print(colorir(f"Erro ao criar commit: {e.stderr.decode('utf-8').strip()}", Fore.RED))
        return

    print(colorir('-----------------------------------------------------------\n', Fore.GREEN))

    try:
        subprocess.run(["git", "push", "origin", "master"], capture_output=True, check=True)
        print(colorir(f'> Comando enviado: "git push origin master"', Fore.CYAN))
        print(colorir('Repositório remoto atualizado.', Fore.CYAN))
    except subprocess.CalledProcessError as e:
        print(colorir(f"Erro ao atualizar repositório remoto: {e.stderr.decode('utf-8').strip()}", Fore.RED))
        return

    print(colorir('-----------------------------------------------------------\n', Fore.GREEN))
    print(colorir('Fim da execução do código', Fore.YELLOW))

def colorir(texto, cor, estilo=Style.NORMAL):
    return f"{cor}{estilo}{texto}{Style.RESET_ALL}"

def titulo():
    os.system('clear')
    print(colorir('--------------------------------------------------------------------', Fore.GREEN))
    print(colorir('|   SISTEMA SIMPLIFICADO DE ENVIO DE ARQUIVOS PARA O GITHUB        |', Fore.GREEN))
    print(colorir('|------------------------------------------------------------------|', Fore.GREEN))
    print(colorir('| 1) Você precisa estar logado em sua conta do git para            |', Fore.YELLOW))
    print(colorir('|    que os comandos funcionem. Use os comandos abaixo:            |', Fore.YELLOW))
    print(colorir('|    git config --global user.name "Nome Completo"                 |', Fore.YELLOW))
    print(colorir('|    git config --global user.email "seuemail@exemplo.com"         |', Fore.YELLOW))
    print(colorir('| 2) Ou use a configuração com token com o comando:                |', Fore.YELLOW))
    print(colorir('|    git config --global credential.helper cache                   |', Fore.YELLOW))
    print(colorir('| 3) O comentário do "commit" no terminal deve estar entre aspas.  |', Fore.YELLOW))
    print(colorir('--------------------------------------------------------------------\n', Fore.GREEN))

def verificar_modificacoes_git():
    try:
        status = subprocess.run(["git", "status"], capture_output=True, text=True, check=True)
        return "nothing to commit, working tree clean" not in status.stdout
    except subprocess.CalledProcessError as e:
        print(colorir(f"Erro ao verificar o status do Git: {e.stderr.decode('utf-8').strip()}", Fore.RED))
        return False

if __name__ == "__main__":
    main()
