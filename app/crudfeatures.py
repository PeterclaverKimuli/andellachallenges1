class User:
    """
    User model class
    """

    def __init__(self, username, password, name=None):
        self.username = username
        self.name = name
        self.password = password
        self.shoppinglists = {}

    def create_shoppinglist(self, shoppinglist):
        """
        Create a shopping list if it does not exist already
        :param shoppinglist:
        :return:
        """
        if shoppinglist.id in self.shoppinglists.keys():
            return False
        else:
            self.shoppinglists[shoppinglist.id] = shoppinglist
            return True

    def update_shoppinglist(self, shoppinglist_id, name):
        """
        This method first checks whether the shopping list exists,
        if it does it changes the shopping list name to the
        new one
        :param shoppinglist_id:
        :param name:
        :return:
        """
        if shoppinglist_id in self.shoppinglists.keys():
            shoppinglist = self.shoppinglists[shoppinglist_id]
            shoppinglist.name = name
            return True
        return False

    def delete_shoppinglist(self, shoppinglist_id):
        """
        Delete a shopping list from the User's shopping lists if
        it exists.
        :param shoppinglist_id:
        :return:
        """
        if shoppinglist_id in self.shoppinglists.keys():
            self.shoppinglists.pop(shoppinglist_id)
            return True
        return False

    def get_shoppinglist(self):
        """
        Get a user's shopping lists
        :return:
        """
        return self.shoppinglists

    def get_shoppinglist(self, shoppinglist_id):
        """
        Get a user's shopping list by Id
        :param shoppinglist_id:
        :return:
        """
        if shoppinglist_id in self.shoppinglists.keys():
            return self.shoppinglists[shoppinglist_id]
        return None


class ShoppingList:
    """
    ShoppingList class
    """

    def __init__(self, shoppinglist_id, name):
        self.id = shoppinglist_id
        self.name = name
        self.items = {}

    def create_item(self, item, quantity):
        """
        Create a shopping list item if it does not already exist
        :param item:
        :return:
        """
        if item.id in self.items.keys():
            return False
        else:
            self.items[item.id] = (item, quantity)
            return True

    def get_item(self, item_id):
        """
        Get the item by its Id
        :param item_id:
        :return:
        """
        if item_id in self.items.keys():
            return self.items[item_id]
        return None

    def update_item(self, item_id, name):
        """
        Method to update the item in the shopping list.
        :param item_id:
        :param name:
        :param description:
        :param deadline:
        :return:
        """
        if item_id in self.items.keys():
            item = self.items[item_id]
            item.name = name
            return True
        return False

    def delete_item(self, item_id):
        """
        Delete an item from the shopping list.
        :param item_id:
        :return:
        """
        if item_id in self.items.keys():
            self.items.pop(item_id)
            return True
        return False


class ShoppingListItem:
    """
    ShoppingListItem class
    """

    def __init__(self, item_id, name):
        self.id = item_id
        self.name = name

