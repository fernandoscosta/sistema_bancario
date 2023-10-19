
'''
Sistema desenvolvido como desafio do curso Estrutura de Dados em Python
Fernando da Silva Costa 
Versao 0.2 - 19 Out 2023

Obs: Para que o programa funcione com as devidas cores no terminal favor instalar o pacote abaixo em seu ambiente venv
pip install colorama
'''

from colorama import init, Fore, Back, Style

init()

max_terminal = 100
prencher = '#'
vazio = ' '
clientes = {}
contas = []
numero_conta = 0
saldo = float(0)
limite = float(500)
extrato = ""
lista_depositos = []
lista_saques = []
LIMITE_SAQUES = int(3)

def menu():
    menu = Back.BLUE + f"""\n{max_terminal * vazio}
    {80 * prencher}{40 * vazio}
        SISTEMA BANCÁRIO{10 * vazio}                                                                                                   
    {80 * prencher}{40 * vazio}
                                                                                                                           
    (1) {Style.BRIGHT}Novo Cliente           {Style.NORMAL}{Fore.LIGHTBLUE_EX}Cadastrar Novo Cliente no Sistema Bancário{Fore.RESET}                                                
    (2) {Style.BRIGHT}Nova Conta Corrente    {Style.NORMAL}{Fore.LIGHTBLUE_EX}Cadastrar Nova Conta no Sistema Bancário{Fore.RESET}           
    (3) {Style.BRIGHT}Depositar              {Style.NORMAL}{Fore.LIGHTBLUE_EX}Entrada de Recursos em Conta Bancária{Fore.RESET}              
    (4) {Style.BRIGHT}Sacar                  {Style.NORMAL}{Fore.LIGHTBLUE_EX}Retirada de Recursos da Conta Bancária{Fore.RESET}          
    (5) {Style.BRIGHT}Extrato                {Style.NORMAL}{Fore.LIGHTBLUE_EX}Saldo de Conta Corrente de uma Conta Bancária{Fore.RESET}          
    (6) {Style.BRIGHT}Listar Clientes        {Style.NORMAL}{Fore.LIGHTBLUE_EX}Listagem de Cliente Cadastrados{Fore.RESET}               
    (9) {Style.BRIGHT}Sair                   {Style.NORMAL}{Fore.LIGHTBLUE_EX}Logout{Fore.RESET}                                        
                                                                                                                           
                                                                                                                            """ + Back.RESET
    return menu

def novo_cliente(clientes, *, nome, nascimento, cpf, logradouro):
    if cpf in clientes:
        print('Cliente já cadastrado com este CPF!')
        return False;

    clientes[cpf] = { 'nome': nome, 'data_nascimento': nascimento, 'cpf': cpf, 'logradouro' : logradouro}
    print('Cliente cadastrado com Sucesso!')

def nova_conta_corrente(clientes, numero_conta, *, cpf_cliente):
    agencia = '0001'
    numero_conta += 1
    nova_conta = [agencia, numero_conta, cpf_cliente]
    contas.append(nova_conta)
    
    print(f"\n######  Nova Conta Corrente criada #######")
    print(f"Cliente: {clientes[cpf_cliente]['nome']} - CPF ({cpf_cliente})")
    print(f"Endereço: {clientes[cpf_cliente]['logradouro']}")
    print(f"#############################\n")
    print(f"###### Dados Bancários ######")
    print(f"Agência: {agencia} \nConta: {numero_conta}")
    print(f"#############################")

def listar_clientes(clientes):
    print(f"Relação de Clientes\n")
    for cliente in clientes:
        print(f"Cliente: {cliente['nome']} - CPF ({cliente['cpf']})")

def deposito(saldo, valor):
    saldo = saldo + valor
    lista_depositos.append(valor)        
    print(Fore.GREEN + "Depósito de R$ {valor} realizado com Sucesso!" + Fore.RESET) 

def saque(*, saldo, valor, limite, limite_saques):
   
    if len(lista_saques) > limite_saques:
        print(Fore.BLUE + f"você excedeu o número de 3 saques diários" + Fore.RESET)
        return False
    
    if valor > limite:
        print(Fore.BLUE + f"Você possui um limite de R$ {limite} por saque." + Fore.RESET)
        return False    
    
    if valor > saldo:
        print(Fore.RED + "Saldo insuficiente!" + Fore.RESET)
        return False
    
    saldo = saldo - valor
    lista_saques.append(valor)
    
    print(Fore.GREEN + "Saque realizado com Sucesso!" + Fore.RESET)

    #saldo e extrato
    return saldo, extrato

def extrato():
    return 0

def validar_valor(valor):
    if "," in valor:
        print(Fore.RED + "Valor inválido. Por favor, não use vírgula." + Fore.RESET)
        return False
        
    if any(c.isalpha() for c in valor):
        print(Fore.RED + "Valor inválido. Por favor, não use letras." + Fore.RESET)
        return False    
    
    if float(valor) < 0:
        print(Fore.RED + "Valor informado inválido!" + Fore.RESET)
        return False
            
    return float(valor)

while True:
    opcao = int(input(menu()))

    if opcao == 1:
        #print(Back.BLUE + f"""##################################################################################################################\n """) 
        print(Back.BLUE + "NOVO CLIENTE")
        
        
        #print(Fore.LIGHTBLUE_EX + "Cadastrar Novo Cliente no Sistema Bancário" + Fore.RESET}   
        nome_cliente = input('Nome do Cliente: ')
        data_nascimento = input('Data de Nascimento: ')
        identificacao = input('CPF: ')
        endereco = input('Endereço: ')   

        #validar dados de entrada do novo cliente 

        novo_cliente(clientes, nome = nome_cliente, nascimento = data_nascimento, cpf = identificacao, logradouro = endereco)

    elif opcao == 2:
        print(Back.BLUE + "Para abertura de Nova Conta Corrente é necessário informar o CPF do Cliente")
        cpf_cliente = input('CPF do Cliente: ')

        if cpf_cliente not in clientes:
            print('Cliente inexistente! - Informe um CPF de um Cliente Válido!')
                
        nova_conta_corrente(clientes, numero_conta, cpf_cliente=cpf_cliente)
        
    elif opcao == 3:
        print(Back.BLUE + "NOVO DEPÓSITO" + 100 * vazio)
        valor = validar_valor(input('Valor do Depósito: '))
        
        if valor == False:
            continue

        deposito(saldo, valor)        
               
    elif opcao == 4:
        valor_saque = validar_valor(input('Valor do Saque: '))

        if valor_saque == False:
            continue

        if saque(saldo = saldo, valor = valor_saque, limite = limite, limite_saques = LIMITE_SAQUES) == False:
            continue
            
    elif opcao == 5:
        print(Fore.LIGHTBLUE_EX + "\n=======  EXTRATO ======" + Fore.RESET)
        if len(lista_depositos) > 0:                  
            for deposito in lista_depositos:
                print(Fore.LIGHTBLUE_EX + f"Depósito: R$ {deposito:.2f}" + Fore.RESET)
        
        if len(lista_saques) > 0:    
            for saque in lista_saques:
                print(Fore.LIGHTBLUE_EX + f"Saque: R$ {saque:.2f}" + Fore.RESET)
            
        print(Fore.LIGHTBLUE_EX + f"Saldo: R$ {saldo:.2f}")  
        print(Fore.LIGHTBLUE_EX + "\n=======================" + Fore.RESET)  
        
    elif opcao == 6:
        listar_clientes(clientes)
                    
    elif opcao == 9:        
        break
    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")