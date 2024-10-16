import datetime

# Variáveis globais
saldo = numero_saques = transacoes = 0
limite = 500
extrato = []

# Constantes
LIMITE_SAQUES = 3
LIMITE_TRANSACOES = 10
        

def validacao():
    global transacoes
    global LIMITE_TRANSACOES
    
    while True:
        if (transacoes < LIMITE_TRANSACOES):
            opcao = int(input('Deseja continuar? [1] Sim, [2] Não '))
            if opcao in [1, 2]:
                return opcao # Retorna o valor para onde a função foi chamada
            else:
                print('Resposta inválida. Tente novamente!')
        else:
            return

def depositar():
    global saldo
    global extrato
    global transacoes
    global LIMITE_TRANSACOES

    while True:
        if (transacoes < LIMITE_TRANSACOES):
            valor = float(input('Informe o valor do depósito: ').replace(',', '.'))

            if (valor > 0):
                saldo += valor
                transacoes += 1
                extrato.append(f"Depósito de R$ {valor:.2f} em {datetime.datetime.now().strftime('%d/%m/%Y %H: %M')}")
            
            elif (valor < 0):
                print('Não é possível depositar valores negativos.')
        
            opcao = validacao()
            if opcao == 2:
                break
        else:
            return
         

def sacar():
    global saldo
    global limite
    global extrato
    global numero_saques
    global LIMITE_SAQUES
    global transacoes
    global LIMITE_TRANSACOES

    while True:
        if (transacoes < LIMITE_TRANSACOES):

            valor = float(input('Informe o valor do saque: ').replace(',', '.'))

            if (valor < limite) and (valor <saldo) and (numero_saques < LIMITE_SAQUES):
                saldo -= valor;
                transacoes += 1
                extrato.append(f"Saque de R$ {valor:.2f} em {datetime.datetime.now().strftime('%d/%m/%Y %H: %M')}")
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
        else:
            return

def imprimirExtrato():
    global transacoes
    global LIMITE_TRANSACOES
    global extrato
    
    if (transacoes < LIMITE_TRANSACOES):
        for i in extrato:
            print(i, end = '\n')
        print(f"Saldo de R$ {saldo:.2f} em {datetime.datetime.now().strftime('%d/%m/%Y %H: %M')}")
        transacoes += 1
    else:
        return


menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

while True:
    if transacoes < LIMITE_TRANSACOES:
        opcao = int(input(menu))
        if opcao == 1:
            depositar()
        elif opcao == 2:
            sacar()
        elif opcao == 3:
            imprimirExtrato()
        elif opcao == 4:
            break
        else:
            print('Opção inválida. Tente novamente.')
    else:
        print('Número de transações diárias excedidas. Volte amanhã.')
        break
