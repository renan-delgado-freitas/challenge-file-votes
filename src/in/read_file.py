def read_file(file="/home/renan/data/in/entrada.dat"):
    data = []
    with open(file, 'r') as file:
        for line in file:
            data.append(line.strip())
        return data


def filter_data(data):
    salesmen = []
    customers = []
    sales = {}

    for line in data:
        item = line.split('ç')
        if item[0] == '001':
            salesmen.append(item)
        elif item[0] == '002':
            customers.append(item)
        elif item[0] == '003':
            sale_id = item[1]
            sale_item = item[2].replace("[", "").replace("]", "").split(",")
            total_sale = sum(float(item.split('-')[1]) * float(item.split('-')[2]) for item in sale_item)
            sales[sale_id] = total_sale
    return salesmen, customers, sales


if __name__ == '__main__':
    print(filter_data(read_file()))
