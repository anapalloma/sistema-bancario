# Variáveis globais
saldo = numero_saques = 0
limite = 500
extrato = []

# Variável imutável
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
    while True:
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato.append(f'Depósito de: R$ {valor:.2f}')
            print(extrato)
        
        else:
            print('Não é possível depositar valores negativos.')
         
        opcao = validacao()
        if opcao == 2:
            break

def sacar():
    global saldo
    global limite
    global numero_saques
    global LIMITE_SAQUES

    while True:
        valor = float(input('Informe o valor do saque: '))

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
        print(extrato)

        opcao = validacao()
        if opcao == 2:
            break
          

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
        extrato()
    elif opcao == 4:
        break
    else:
        print('Opção inválida. Tente novamente.')
