# Variáveis globais
saldo = numero_saques = 0
limite = 500
extrato = []

# Constantes
LIMITE_SAQUES = 3
        

def validacao():
    while True:
        opcao = int(input('Deseja continuar? [1] Sim, [2] Não '))
        if opcao in [1, 2]:
            return opcao # Retorna o valor para onde a função foi chamada
        else:
            print('Resposta inválida. Tente novamente!')

def depositar():
    global saldo
    global extrato

    while True:
        valor = float(input('Informe o valor do depósito: ').replace(',', '.'))

        if valor > 0:
            saldo += valor
            extrato.append(f'Depósito de: R$ {valor:.2f}')
        
        else:
            print('Não é possível depositar valores negativos.')
         
        opcao = validacao()
        if opcao == 2:
            break

def sacar():
    global saldo
    global limite
    global extrato
    global numero_saques
    global LIMITE_SAQUES

    while True:
        valor = float(input('Informe o valor do saque: ').replace(',', '.'))

        if (valor < limite) and (valor <saldo) and (numero_saques < LIMITE_SAQUES):
            saldo -= valor;
            extrato.append(f'Saque: R$ {valor:.2f}')
            numero_saques += 1
        
        elif valor > limite:
            print('Operação não permitida. Valor excede ao limite disponível na conta.')
        
        elif valor > saldo:
            print('Operação não permitida. Saldo insuficiente.')
        
        elif numero_saques > LIMITE_SAQUES:
            print('Operação não permitida. Quantidade diária de saques excedida.')

        opcao = validacao()
        if opcao == 2:
            break   

def imprimir_extrato():
    global extrato
    for i in extrato:
            print(i, end = '\n')
    print(f'Saldo: R$ {saldo:.2f}')


menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

while True:
    opcao = int(input(menu))
    if opcao == 1:
        depositar()
    elif opcao == 2:
        sacar()
    elif opcao == 3:
        imprimir_extrato()
    elif opcao == 4:
        break
    else:
        print('Opção inválida. Tente novamente.')
