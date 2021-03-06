import unittest
from app.crudfeatures import User
from app.shoppinglistapp import ShoppingListApp


class TestUserAuthentication(unittest.TestCase):
    """
    Class to test the user authentication, both the registration
    and login.
    """

    def setUp(self):
        self.user = User('sanduxy', '12345678', 'Sandra')
        self.app = ShoppingListApp()

    def test_user_is_added_to_dictionary_when_created(self):
        self.assertTrue(self.app.register_user(User('sandux', '12345678', 'Sandra')))

    def test_user_already_exists_in_user_dictionary(self):
        self.app.users = {'sanduxy': self.user}
        self.assertFalse(self.app.register_user(self.user))

    def test_user_sigining_in_is_already_registered(self):
        self.app.users = {'sanduxy': self.user}
        self.assertTrue(self.app.does_user_exist('sanduxy'))

    def test_user_trying_to_login_has_entered_a_correct_password(self):
        self.app.users = {'sanduxy': self.user}
        self.assertTrue(self.app.login_user('sanduxy', '12345678'))

    def test_user_trying_to_login_has_entered_a_wrong_password(self):
        self.app.users = {'sanduxy': self.user}
        self.assertFalse(self.app.login_user('sanduxy', '12341'))


if __name__ == '__main__':
    unittest.main()