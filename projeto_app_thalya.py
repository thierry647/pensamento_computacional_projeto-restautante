'''

CRUD

restaurante 

o sistema vai gerenciar o restaurante, seus adjacentes como exemplo: estoque,funcionarios, caixas, avaliação do
restaurante e pedidos de delivery.  

'''


print('Bem vindo!')

# input('Prensione Enter para sair...')

nome_usuario = input('Digite seu nome:')

print('\n'+"_"*30)

print(f"ola, {nome_usuario}, Seja bem-vindo(a)")

email_usuario = input('Digite seu email:')

senha_usuario = input('Digite sua senha:')

endereco_usuario = input('Digite seu endereco:')

telefone_usuario = input('Digite seu telefone:')

print('\n'+"_"*30)

print('O que deseja fazer?')

print('1 - Acessar Delivery')

print('2 - Fazer reserva')

print('3 - Ver menu ')

print('4 - ver cardapio')
 
print('5 - avaliar restaurante')

print('0 - sair')
'''
while True: 
    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        print('acessando Delivery...')
        
        break 
    elif opcao == '2':
        print('Fazendo reserva...')

        break
    elif opcao == '3':
        print('verificando menu...')

        break
    elif opcao == '4':

'''

while True:
    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        print('Acessando Delivery...')
        print('Cardápio: 1- Feijoada Individual | 2- Feijoada Família')
        prato = input('Qual o número do prato? ')
        endereco = input('Digite o endereço de entrega: ')
        pagamento = input('Forma de pagamento (Pix/Cartão): ')
        print(f'\n✅ Pedido realizado! Você escolheu a opção {prato}.')
        print(f'Será entregue em: {endereco}')
        break
    elif opcao == '2':
        print('Fazendo reserva...')
        print('\n--- 📅 FAZENDO RESERVA ---')
        data = input('Qual a data da reserva? ')
        pessoas = input('Para quantas pessoas? ')
        print(f'Reserva feita para {pessoas} pessoas no dia {data}!')
        break
    elif opcao == '3':
        print('Verificando menu...')
        print('\n--- 📋 NOSSO MENU COMPLETO ---')
        print('Entradas: Torresmo, Caldinho de Feijão')
        print('Prato Principal: Feijoada Completa')
        print('Bebidas: Suco de Laranja, Refrigerante')
        input('\nPressione ENTER para voltar ao menu...')
        break
    elif opcao == '4':
        print('\n--- 💰 TABELA DE PREÇOS ---')
        print('Feijoada Individual: R$ 35,00')
        print('Feijoada Família: R$ 90,00')
        print('Torresmo Porção: R$ 15,00')
        input('\nPressione ENTER para voltar ao menu...')
        break
    elif opcao == '5':
        print('Avaliando restaurante...')
        nota = input('De 0 a 5, qual nota você nos dá? ')
        comentario = input('Deixe um breve comentário: ')
        print(f'Obrigado! Você deu nota {nota}. Isso nos ajuda muito!')
        break
    elif opcao == '0':
        print('Saindo...')
        break
    else:
        print('Opção inválida. Por favor, tente novamente.')