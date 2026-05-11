import unittest
from app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_response_contains_warrior(self):
        response = self.client.get('/')
        self.assertIn('Warrior', response.data.decode('utf-8'))

    def test_response_not_empty(self):
        response = self.client.get('/')
        self.assertTrue(len(response.data) > 0)

    def test_response_type_is_string(self):
        response = self.client.get('/')
        self.assertIsInstance(response.data.decode('utf-8'), str)

if __name__ == '__main__':
    unittest.main()
