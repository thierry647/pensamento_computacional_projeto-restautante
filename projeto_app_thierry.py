'''

  CRUD

  Restaurante

 o sistrema vai gerenciar o restaurante, e seus adjacentes como exemplo: estoque, funcinarios, caixa, avaliação do restaurante 
 e pedidos de delivery. 

'''


print('Bem vindo ao restaurante!!')

nome_usuario = input('Digite seu nome: ')
print('\n' + "_"*30)
print(f"ola {nome_usuario}, seja bem vindo")

email_usuario = input('Digite seu email: ')
senha_usuario = input('Digite sua senha: ')
endereco_usuario = input('Digite seu endereço: ')
telefone_usuario = input('Digite seu telefone: ')

print('\n' + "_"*30)

import uuid
import secrets

# Função para gerar chave Pix aleatória
def gerar_chave_pix():
    return str(uuid.uuid4())

# Simular criação de um código de pagamento Pix
def gerar_codigo_pix(valor, banco, descricao="Pagamento via Pix"):
    chave = gerar_chave_pix()
    txid = secrets.token_hex(5)  # identificador único da transação
    codigo = {
        "banco": banco,
        "valor": valor,
        "descricao": descricao,
        "chave_pix": chave,
        "txid": txid
    }
    return codigo

while True:
    print('\nO que deseja fazer?')
    print('1 - Acessar Delivery')
    print('2 - Fazer reserva')
    print('3 - Ver menu')
    print('4 - Ver cardápio')
    print('5 - Avaliar restaurante')
    print('0 - Sair')

    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        print('Acessando Delivery...')
        print('Cardápio: 1- Feijoada Individual | 2- Feijoada Família')
        prato = input('Qual o número do prato? ')
        endereco = input('Digite o endereço de entrega: ')
        pagamento = input('Forma de pagamento (Pix/Cartão): ')

        if pagamento.lower() == "pix":
            valor = 35.00 if prato == "1" else 90.00
            pedido = gerar_codigo_pix(valor, "Banco do Brasil", "Compra de Feijoada")
            print("\n✅ Pedido realizado com Pix!")
            print(f"Valor: R$ {pedido['valor']:.2f}")
            print(f"Chave Pix gerada: {pedido['chave_pix']}")
            print(f"TxID da transação: {pedido['txid']}")
        else:
            print(f'\n✅ Pedido realizado! Você escolheu a opção {prato}.')
            print(f'Será entregue em: {endereco}')

    elif opcao == '2':
        print('\n--- 📅 FAZENDO RESERVA ---')
        data = input('Qual a data da reserva? ')
        pessoas = input('Para quantas pessoas? ')
        print(f'Reserva feita para {pessoas} pessoas no dia {data}!')

    elif opcao == '3':
        print('\n--- 📋 NOSSO MENU COMPLETO ---')
        print('Entradas: Torresmo, Caldinho de Feijão')
        print('Prato Principal: Feijoada Completa')
        print('Bebidas: Suco de Laranja, Refrigerante')
        input('\nPressione ENTER para voltar ao menu...')

    elif opcao == '4':
        print('\n--- 💰 TABELA DE PREÇOS ---')
        print('Feijoada Individual: R$ 35,00')
        print('Feijoada Família: R$ 90,00')
        print('Torresmo Porção: R$ 15,00')
        input('\nPressione ENTER para voltar ao menu...')

    elif opcao == '5':
        print('Avaliando restaurante...')
        nota = input('De 0 a 5, qual nota você nos dá? ')
        comentario = input('Deixe um breve comentário: ')
        print(f'Obrigado! Você deu nota {nota}. Isso nos ajuda muito!')

    elif opcao == '0':
        print('Saindo...')
        break

    else:
        print('Opção inválida. Por favor, tente novamente.')
