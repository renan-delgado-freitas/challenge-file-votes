import os


def ler_arquivos(arquivo='/home/renan/data/in/entrada.dat'):
    dados = []
    with open(arquivo, 'r') as arquivo:
        for linha in arquivo:
            dados.append(linha.strip())
        return dados


def filtrar_dados(dados):
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
            venda_total = sum(float(item.split('-')[1]) * float(item.split('-')[2]) for item in venda_items)
            vendas[venda_id] = venda_total
    return clientes, vendedores, vendas


if __name__ == '__main__':
    print(filtrar_dados(ler_arquivos()))
