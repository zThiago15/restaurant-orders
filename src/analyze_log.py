import csv
import os


def analyze_log(path_to_file):

    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    if not os.path.isfile(path_to_file):
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    with open(path_to_file) as file:
        orders = list(csv.reader(file))
        items = {order[1] for order in orders}
        days = {order[2] for order in orders}

        arnaldo_hamburger_orders = sum(
            1 for order in orders if order[0] == 'arnaldo'
            and order[1] == 'hamburguer')

        joao_ordered_items = {order[1] for order in orders if order[0] == 'joao'}
        joao_never_ordered_items = items - joao_ordered_items
        joao_ordered_days = {order[2] for order in orders if order[0] == 'joao'}
        days_joao_never_ordered = days - joao_ordered_days

        maria_items = [item for item in orders if item[0] == 'maria']
        maria_most_ordered_item = max(
            set(item[1] for item in maria_items),
            key=[item[1] for item in maria_items].count
        )

    with open('data/mkt_campaign.txt', "w") as file:
        print(maria_most_ordered_item, file=file)
        print(arnaldo_hamburger_orders, file=file)
        print(joao_never_ordered_items, file=file)
        print(days_joao_never_ordered, file=file)
