import unittest
from app.crudfeatures import ShoppingList
from app.crudfeatures import ShoppingListItem


class TestShoppingListItems(unittest.TestCase):
    def setUp(self):
        self.shoppinglist = ShoppingList("01", "Books")

    def test_user_can_create_shoppinglist(self):
        item = ShoppingListItem('02', 'Pens')
        self.assertTrue(self.shoppinglist.create_item(item, 3))

    def test_item_already_exists_in_the_shoppinglist(self):
        item = ShoppingListItem('02', 'Pens')
        self.shoppinglist.items = {'Pens': item}
        self.assertTrue(self.shoppinglist.create_item(item, 3))

    def test_an_item_in_the_shoppinglist_is_returned_when_an_id_is_specified(self):
        item = ShoppingListItem('02', 'Pens')
        self.shoppinglist.items = {'02': item}
        self.assertEqual(self.shoppinglist.get_item(item.id), item)

    def test_none_is_returned_when_an_item_is_not_found_by_its_id(self):
        self.assertIsNone(self.shoppinglist.get_item("04"))

    def test_that_an_item_in_a_shoppinglist_is_updated(self):
        item = ShoppingListItem('02', 'Pens')
        self.shoppinglist.items = {'02': item}
        self.shoppinglist.update_item('02', 'Pencils')
        self.assertEqual(self.shoppinglist.get_item('02').name, 'Pencils')

    def test_item_to_be_updated_is_missing(self):
        self.assertFalse(self.shoppinglist.update_item('04', 'Pens'))

    def test_item_is_successfully_deleted(self):
        item = ShoppingListItem('02', 'Pens')
        self.shoppinglist.items = {'02': item}
        self.shoppinglist.delete_item('02')
        self.assertEqual(self.shoppinglist.items, {})

    def test_an_item_that_does_not_exist_cannot_be_deleted(self):
        self.assertFalse(self.shoppinglist.delete_item("07"))


if __name__ == '__main':
    unittest.main()
