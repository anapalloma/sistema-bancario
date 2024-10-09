# Variáveis globais
saldo = numero_saques = 0
limite = 500
extrato = []
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
