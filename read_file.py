def read_file(file="data/in/entrada.dat"):
    data = []
    with open(file, 'r') as file:
        for line in file:
            data.append(line.strip())
    return data


def filter_data(data):
    sellers = []
    customers = []
    sales = {}

    for line in data:
        item = line.split('ç')
        if item[0] == '001':
            sellers.append(item)
        elif item[0] == '002':
            customers.append(item)
        elif item[0] == '003':
            sale_id = item[1]
            name = item[-1]
            sale_item = item[2].replace("[", "").replace("]", "").split(",")
            total_sale = sum(float(item.split('-')[1]) * float(item.split('-')[2]) for item in sale_item)
            sales[sale_id] = total_sale, name

    return sellers, customers, sales


def create_report(seller, customers, sales):
    worst_seller = sales.get(min(sales, key=sales.get))[1]

    with open("data/out/report.done.dat", 'w') as file:
        file.write(f'Quantidade de vendedor no arquivo de entrada: {len(seller)}\n')
        file.write(f'Quantidade de clientes no arquivo de entrada: {len(customers)}\n')
        file.write(f'ID da venda mais cara: {max(sales, key=sales.get)}\n')
        file.write(f'O pior vendedor: {worst_seller}\n')


# Funcao criada apenas para testar o retorno do codigo
def sales_per_salesman(sales):
    for seller in sales:
        print(seller, ": ", sales[seller])
