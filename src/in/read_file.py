import os


def read_file(arquivo='/home/renan/src/in/entrada.dat'):
    dados = []
    with open(arquivo, 'r') as file:
        for line in file:
            dados.append(line.strip())
    return dados


def processar_dados(dados):
    clientes = []
    vendedores = []
    vendas = {}

    for linha in dados:
        item = linha.split('ç')
        if item[0] == '001':
            clientes.append(item)
        elif item[0] == '002':
            vendedores.append(item)
        elif item[0] == '003':
            venda_id = item[1]
            venda_items = item[2].replace('[', '').replace(']', '').split(',')
            total_venda = sum(float(item.split('-')[1]) * float(item.split('-')[2]) for item in venda_items)
            vendas[venda_id] = total_venda

    return clientes, vendedores, vendas


if __name__ == '__main__':
    print(processar_dados(read_file()))


