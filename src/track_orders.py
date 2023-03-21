class TrackOrders:
    def __init__(self):
        self.orders = []

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append({
            "customer": customer,
            "order": order,
            "day": day
        })

    def get_most_ordered_dish_per_customer(self, customer):
        dishes = [order["order"] for order in self.orders if order["customer"] == customer]
        return max(set(dishes), key=dishes.count)

    def get_never_ordered_per_customer(self, customer):
        all_dishes = set(order["order"] for order in self.orders)
        ordered_dishes = set(order["order"] for order in self.orders if order["customer"] == customer)
        return all_dishes - ordered_dishes

    def get_days_never_visited_per_customer(self, customer):
        all_days = set(order["day"] for order in self.orders)
        visited_days = set(order["day"] for order in self.orders if order["customer"] == customer)
        return all_days - visited_days

    def get_busiest_day(self):
        days = [order["day"] for order in self.orders]
        return max(set(days), key=days.count)

    def get_least_busy_day(self):
        days = [order["day"] for order in self.orders]
        return min(set(days), key=days.count)
