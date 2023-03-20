from typing import Dict, Set
import csv


def analyze_log(path_to_file: str):
    if not path_to_file.lower().endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, 'r') as f:
            orders = f.read().splitlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    with open(path_to_file) as file:
        orders = list(csv.reader(file))
        items = {order[1] for order in orders}
        days = {order[2] for order in orders}

        arnaldo_hamburger_orders = 0
        for order in orders:
            if order[0] == 'arnaldo' and order[1] == 'hamburguer':
                arnaldo_hamburger_orders += 1

        joao_ordered_items = set()
        for order in orders:
            if order[0] == 'joao':
                joao_ordered_items.add(order[1])
        joao_never_ordered_dishes = items - joao_ordered_items

        joao_ordered_days = set()
        for order in orders:
            if order[0] == 'joao':
                joao_ordered_days.add(order[2])
        days_joao_never_ordered = days - joao_ordered_days

        maria_items = []
        for order in orders:
            if order[0] == 'maria':
                maria_items.append(order)
        maria_most_ordered_dish = max(set(item[1] for item in maria_items), key=[item[1] for item in maria_items].count)

    with open('data/mkt_campaign.txt', "w") as file:
        print(maria_most_ordered_dish, file=file)
        print(arnaldo_hamburger_orders, file=file)
        print(joao_never_ordered_dishes, file=file)
        print(days_joao_never_ordered, file=file)
