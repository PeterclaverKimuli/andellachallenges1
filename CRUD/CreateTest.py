import unittest
import Create

class TestCreate(unittest.TestCase):
    def setUp(self):
        self.shoppingitem = Create.Create()

    def test_createlist(self):
        self.shoppingitem.create_list('Campus', 'Books', 3, 500)
        self.assertEqual(self.shoppingitem.name, 'Campus', msg="The list name should be a string")
        self.assertEqual(self.shoppingitem.list_items, {'Books': [3, 1500]}, msg="Dictionary should have the item name and a list of quantity and the total cost")
        self.assertEqual(self.shoppingitem.save_lists, [{'Books': [3, 1500]}], msg="The dictionary containing the list should be saved here.")

    def test_readlist(self):
        self.assertEqual(self.shoppingitem.read_list('Camp'), 'Invalid shopping list', msg="The print statement is wrong")

    def test_updatelist(self):
        self.assertEqual(self.shoppingitem.update_list('Camp', 'Books', 2, 500), 'Invalid shopping list', msg="The print statement is wrong")

    def test_deletelist(self):
        self.shoppingitem.list_items = {'Books': [3, 1500]}
        self.shoppingitem.delete_item('Books')
        self.assertEqual(self.shoppingitem.list_items, {}, msg="The dictionary is supposed to be empty.")