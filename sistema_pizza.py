valor = 0
sabor = ''

print('-----------Bem-vindo à Pizzaria do Elias Lorandi----------')
print('-------------------------CARDÁPIO-------------------------')
print('| Código | Descrição  | Pizza Média(M) | Pizza Grande(G) |')
print('|   21   | Napolitana |    R$ 20,00    |     R$ 26,00    |')
print('|   22   | Margherita |    R$ 20,00    |     R$ 26,00    |')
print('|   23   | Calabresa  |    R$ 25,00    |     R$ 32,50    |')
print('|   24   | Toscana    |    R$ 30,00    |     R$ 39,00    |')
print('|   25   | Portuguesa |    R$ 30,00    |     R$ 39,00    |')
print('----------------------------------------------------------')

while True:
    # achei mais organizado colocar o sabor antes do tamanho
    codigo = input('Entre com o código do sabor desejado: ')
    # o texto que for digitado, ficará em maiúsculo
    tamanho = input('Entre com o tamanho da pizza (M/G): ').upper()
    if tamanho == 'm' and 'g':
        print('Operação inválida!')
        continue
    if codigo == '21' and tamanho == 'M':
        valor = valor + 20  # variaveis 'valor' e 'sabor' estão no topo do código
        sabor = sabor + 'Napolitana \n'
    elif codigo == '21' and tamanho == 'G':
        valor = valor + 26
        sabor = sabor + 'Napolitana \n'
    elif codigo == '22' and tamanho == 'M':
        valor = valor + 20
        sabor = sabor + 'Margherita \n'
    elif codigo == '22' and tamanho == 'G':
        valor = valor + 26
        sabor = sabor + 'Margherita \n'
    elif codigo == '23' and tamanho == 'M':
        valor = valor + 25
        sabor = sabor + 'Calabresa \n'
    elif codigo == '23' and tamanho == 'G':
        valor = valor + 32.50
        sabor = sabor + 'Calabresa \n'
    elif codigo == '24' and tamanho == 'M':
        valor = valor + 30
        sabor = sabor + 'Toscana \n'
    elif codigo == '24' and tamanho == 'G':
        valor = valor + 39
        sabor = sabor + 'Toscana \n'
    elif codigo == '25' and tamanho == 'M':
        valor = valor + 30
        sabor = sabor + 'Portuguesa \n'
    elif codigo == '25' and tamanho == 'G':
        valor = valor + 39
        sabor = sabor + 'Portuguesa \n'
    else:
        print('Operação inválida!')
        continue  # volta para o início do laço
    print('Você pediu a(s) pizza(s):\n' + sabor)
    # pode ser qualquer outro caractere para ser não
    resp = input('Deseja algo mais? \n 1-Sim \n 2-Não \n>> ')
    if resp == '1':
        continue  # volta para o início do laço
    else:
        print('O total a ser pago é: R$ {}' .format(valor))
        break  # fim
