import unittest

class TestAccountRepository(unittest.TestCase):
    def test_store_account_data(self):
        # Simulate storing account data
        account_data = {'id': 1, 'name': 'John Doe'}
        self.assertTrue(store_account_data(account_data))

    def test_retrieve_account_data(self):
        # Simulate retrieving account data
        expected_data = {'id': 1, 'name': 'John Doe'}
        self.assertEqual(retrieve_account_data(1), expected_data)

if __name__ == '__main__':
    unittest.main()