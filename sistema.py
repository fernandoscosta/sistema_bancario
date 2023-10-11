
'''
Sistema desenvolvido como desafio do curso Fundamentos do Python
Fernando da Silva Costa - 11 Out 2023
'''

menu = """
############################
      SISTEMA BANCÁRIO
############################

(d) Depositar
(s) Sacar
(e) Extrato
(q) Sair

=> """

saldo = float(0)
limite = float(500)
extrato = ""
lista_depositos = []
lista_saques = []
LIMITE_SAQUES = int(3)

''' funcao para validar valores de entrada '''
def validarValor(valor):
    if "," in valor:
        print("Valor inválido. Por favor, não use vírgula.")
        return False
        
    if any(c.isalpha() for c in valor):
        print("Valor inválido. Por favor, não use letras.")
        return False    
    
    if float(valor) < 0:
        print("Valor informado inválido!")
        return False
            
    return float(valor)

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = validarValor(input('Valor do Depósito: '))
        
        if valor == False:
            continue
                
        saldo = saldo + valor
        lista_depositos.append(valor)        
        print(f"Depósito de R$ {valor} realizado com Sucesso!")        

    elif opcao == "s":
        valor_saque = validarValor(input('Valor do Saque: '))
                
        if len(lista_saques) > LIMITE_SAQUES:
            print(f"você excedeu o número de 3 saques diários")
            continue
        
        if valor_saque > limite:
            print(f"Você possui um limite de R$ {limite} por saque.")
            continue    
        
        if valor_saque > saldo:
            print(f"Saldo insuficiente!")
            continue
        
        saldo = saldo - valor_saque
        lista_saques.append(valor_saque)
        print("Saque")
        
    elif opcao == "e":
        print("\n=======  EXTRATO ======")
        if len(lista_depositos) > 0:                  
            for deposito in lista_depositos:
                print(f"Depósito: R$ {deposito:.2f}")
        
        if len(lista_saques) > 0:    
            for saque in lista_saques:
                print(f"Saque: R$ {saque:.2f}")
            
        print(f"Saldo: R$ {saldo:.2f}")  
        print("\n=======================")  
                    
    elif opcao == "q":        
        break
    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")