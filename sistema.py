
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
        print('\tCliente já cadastrado com este CPF!')
        return False;

    clientes[cpf] = { 'nome': nome, 'data_nascimento': nascimento, 'cpf': cpf, 'logradouro' : logradouro}
    print('\tCliente cadastrado com Sucesso!')

def nova_conta_corrente(clientes, numero_conta, *, cpf_cliente):
    agencia = '0001'
    numero_conta += 1
    nova_conta = [agencia, numero_conta, cpf_cliente]
    contas.append(nova_conta)
    
    print(f"\n######  Nova Conta Corrente criada #######")
    print(f"\tCliente: {clientes[cpf_cliente]['nome']} - CPF ({cpf_cliente})")
    print(f"\tEndereço: {clientes[cpf_cliente]['logradouro']}")
    print(f"\t#############################\n")
    print(f"\t###### Dados Bancários ######")
    print(f"\tAgência: {agencia} \nConta: {numero_conta}")
    print(f"\t#############################")

def listar_clientes(clientes):
    print(f"\tRelação de Clientes\n")
    for chave, cliente in clientes.items():
        print(f"Cliente: {cliente['nome']} - CPF ({chave})")

def deposito(saldo, valor):
    saldo = saldo + valor
    lista_depositos.append(valor)        
    print(Fore.GREEN + f"\tDepósito de R$ {valor} realizado com Sucesso!" + Fore.RESET) 

def saque(*, saldo, valor, limite, limite_saques):
   
    if len(lista_saques) > limite_saques:
        print(Fore.BLUE + f"\tVocê excedeu o número de 3 saques diários" + Fore.RESET)
        return False
    
    if valor > limite:
        print(Fore.BLUE + f"\tVocê possui um limite de R$ {limite} por saque." + Fore.RESET)
        return False    
    
    if valor > saldo:
        print(Fore.RED + "\tSaldo insuficiente!" + Fore.RESET)
        return False
    
    saldo = saldo - valor
    lista_saques.append(valor)
    
    print(Fore.GREEN + "\tSaque realizado com Sucesso!" + Fore.RESET)

    #saldo e extrato
    return saldo, extrato

def extrato():
    return 0

def validar_valor(valor):
    if valor is '':
        print(Fore.RED + "\tValor não Informado!" + Fore.RESET)
        return False
        
    if "," in valor:
        print(Fore.RED + "\tValor inválido. Por favor, não use vírgula." + Fore.RESET)
        return False
        
    if any(c.isalpha() for c in valor):
        print(Fore.RED + "\tValor inválido. Por favor, não use letras." + Fore.RESET)
        return False    
    
    if float(valor) < 0:
        print(Fore.RED + "\tValor informado inválido!" + Fore.RESET)
        return False
            
    return float(valor)

while True:
    opcao = input(menu())
        
    if opcao in '' or not opcao.isdigit():
        print(Fore.RED + "\tValor informado inválido!" + Fore.RESET)
        continue
    
    opcao = int(opcao)

    if opcao == 1:
        print(Back.BLUE + "\tNOVO CLIENTE" + 130 * vazio)
        nome_cliente = input('\tNome do Cliente: ')
        
        if nome_cliente is '':
            print(Fore.RED + "\tNome do Cliente não Informado!" + Fore.RESET)
            continue
        
        data_nascimento = input('\tData de Nascimento: ')
        
        if data_nascimento is '':
            print(Fore.RED + "\tData de Nascimento não Informado!" + Fore.RESET)
            continue
        
        identificacao = input('\tCPF: ')
        
        if identificacao is '':
            print(Fore.RED + "\tCPF não Informado!" + Fore.RESET)
            continue
        
        endereco = input('\tEndereço: ')   
        
        if endereco is '':
            print(Fore.RED + "\tEndereço não Informado!" + Fore.RESET)
            continue
        
        novo_cliente(clientes, nome = nome_cliente, nascimento = data_nascimento, cpf = identificacao, logradouro = endereco)

    elif opcao == 2:
        print(Back.BLUE + "\tPara abertura de Nova Conta Corrente é necessário informar o CPF do Cliente")
        cpf_cliente = input('\tCPF do Cliente: ')
        
        if cpf_cliente is '':
            print(Fore.RED + "\tCPF do Cliente!" + Fore.RESET)
            continue

        if cpf_cliente not in clientes:
            print('\tCliente inexistente! - Informe um CPF de um Cliente Válido!')
                
        nova_conta_corrente(clientes, numero_conta, cpf_cliente=cpf_cliente)
        
    elif opcao == 3:
        print(Back.BLUE + "\tNOVO DEPÓSITO" + 100 * vazio)
        valor = validar_valor(input('\tValor do Depósito: '))
        
        if valor == False:
            continue

        deposito(saldo, valor)        
               
    elif opcao == 4:
        valor_saque = validar_valor(input('\tValor do Saque: '))

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
        print("\tOperação Inválida, por favor selecione novamente a operação desejada.")
        
