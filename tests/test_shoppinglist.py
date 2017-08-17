import unittest
from app.crudfeatures import User, ShoppingList


class TestUserShoppingList(unittest.TestCase):
    def setUp(self):
        self.user = User('aduweSandra', '12345')

    def test_user_can_create_shoppinglist(self):
        shoppinglist = ShoppingList("01", "Books")
        self.assertTrue(self.user.create_shoppinglist(shoppinglist))

    def test_user_shoppinglist_already_exists(self):
        shoppinglist = ShoppingList("01", "Books")
        self.user.shoppinglists = {"01": shoppinglist}
        self.assertFalse(self.user.create_shoppinglist(shoppinglist))

    def test_a_shoppinglist_is_returned_when_an_id_is_specified(self):
        shoppinglist = ShoppingList("01", "Books")
        self.user.shoppinglists = {"01": shoppinglist}
        self.assertEqual(self.user.get_shoppinglist("01"), shoppinglist)

    def test_none_is_returned_for_a_shoppinglist_that_does_not_exist(self):
        self.assertIsNone(self.user.get_shoppinglist("01"))

    def test_a_shoppinglist_is_updated(self):
        shoppinglist = ShoppingList("01", "Books")
        self.user.shoppinglists = {"01": shoppinglist}
        self.user.update_shoppinglist("01", 'Pencils')
        self.assertEqual(self.user.get_shoppinglist("01").name, "Pencils")

    def test_the_shoppinglist_to_be_updated_does_not_exist(self):
        self.assertFalse(self.user.update_shoppinglist("03", "Pens"))

    def test_a_shoppinglist_is_successfully_deleted(self):
        shoppinglist = ShoppingList("01", "Books")
        self.user.shoppinglists = {"01": shoppinglist}
        self.user.delete_shoppinglist("01")
        self.assertEqual(self.user.shoppinglists, {})

    def test_false_is_returned_when_deleting_un_existing_shoppinglist(self):
        self.assertFalse(self.user.delete_shoppinglist("01"))


if __name__ == '__main__':
    unittest.main()
