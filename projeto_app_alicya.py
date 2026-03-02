'''

CRUD

Restaurante

o sistema vai gerenciar o restaurante, seus adjacentes como por exemplo: estoque, funcionarios, caixas, avaliação do
resturante e pedidos de delivery.

'''


print('Bem-vindo a interface inicial')

nome_usuario = input('Digite seu primeiro nome para começar:')

print(f'olá, {nome_usuario}! Seja bem-vindo(a) ao nosso Resturante')

print('\n' + "_"*25)

email_usuario = input('Digite Seu email de Usuario:')

senha_usuario = input('Digite Sua Senha:')

endereço_usuario = input('Digite Seu Endereço:')

telefone_usuario = input('Digite Seu Telefone:')

print('\n' + "_"*30)

print('O que deseja fazer?')

print('1 - Acessar Delivery')

print('2 - Fazer reserva')

print('3 - Ver Menu')

print('4 -  Ver Cardápio')

print('5 - Avaliar Restaurante')

print('0 - Sair')

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
