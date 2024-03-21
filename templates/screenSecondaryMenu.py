from scripts.global_functions import color, input_caracter, Fore, main_title, get_user_input, validar_entrada


def ScreenSecondaryMenu():
    itens = ['Enviar arquivos para o git', 'Digitar comandos do git', 'Ajuda', 'Sobre', 'Sair']
    main_title()
    pipeGreen = color('|', Fore.GREEN)
    
    print(color(f'  {pipeGreen}{input_caracter(" ", 4)}{pipeGreen}', Fore.YELLOW))

    for count, item in enumerate(itens, start=1):
        print(f'  {pipeGreen}\t{color("[", Fore.YELLOW)}{color(count, Fore.GREEN)}{color("]", Fore.YELLOW)} {color(item, Fore.YELLOW)} {input_caracter(" ", (len(item) + 15))} {pipeGreen}')

    print(color(f'  {pipeGreen}{input_caracter(" ", 4)}{pipeGreen}', Fore.YELLOW))
    print(color(f'  {pipeGreen}{input_caracter(" ", 4)}{pipeGreen}', Fore.YELLOW))
    print(f'  {pipeGreen}\t{color("Digite abaixo a opção desejada:", Fore.YELLOW)}{input_caracter(" ", 40)}{pipeGreen}')
    print(color(f'  {pipeGreen}{input_caracter(" ", 4)}{pipeGreen}', Fore.YELLOW))
    print(color(f'  {input_caracter("—", 2)}', Fore.GREEN))

    validar_entrada(itens)

    