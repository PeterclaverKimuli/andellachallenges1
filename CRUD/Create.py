class Create:
    def __init__(self):
        self.total = 0
        self.list_items = {}
        self.name = ''
        self.save_lists = []


    def create_list(self, list_name, item_name, quantity, cost_of_each):
        self.name = list_name
        self.price = cost_of_each * quantity
        self.list_items[item_name] = [quantity, self.price]
        self.save_lists.append(self.list_items)

    def read_list(self, name1):
        if name1 is self.name:
            print(self.list_items)
        else:
            return 'Invalid shopping list'

    def update_list(self, name2, item_name, quantity1, cost_of_each):
        if name2 is self.name:
            self.price = cost_of_each * quantity1
            self.list_items[item_name] = [quantity1, self.price]
        else:
            return 'Invalid shopping list'

    def delete_item(self, item_name):
        del self.list_items[item_name]

