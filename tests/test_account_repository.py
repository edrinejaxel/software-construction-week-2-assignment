import unittest
from Infrastructure_layer.Repositories.account import AccountRepository
from domain.entities.account import Account

class TestAccountRepository(unittest.TestCase):
    def setUp(self):
        # Create a test account
        self.test_account = Account(1, 100.0, "test_owner")
        self.repository = AccountRepository([self.test_account])

    def test_store_account_data(self):
        # Test storing account data
        account = Account(2, 200.0, "test_owner_2")
        self.repository._accounts[account.account_id] = account
        self.assertTrue(account.account_id in self.repository._accounts)

    def test_retrieve_account_data(self):
        # Test retrieving account data
        retrieved_account = self.repository.get_account(1)
        self.assertEqual(retrieved_account.account_id, self.test_account.account_id)
        self.assertEqual(retrieved_account.balance, self.test_account.balance)

if __name__ == '__main__':
    unittest.main()