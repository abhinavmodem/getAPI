import unittest
from flask import Flask
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_get_test_word(self):
        response = self.client.get('http://localhost:5000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Test')

    def test_post_request(self):
        response = self.client.post('http://localhost:5000/')
        self.assertEqual(response.status_code, 405)  # Method not allowed

    def test_put_request(self):
        response = self.client.put('http://localhost:5000/')
        self.assertEqual(response.status_code, 405)  # Method not allowed

    def test_delete_request(self):
        response = self.client.delete('http://localhost:5000/')
        self.assertEqual(response.status_code, 405)  # Method not allowed

if __name__ == '__main__':
    unittest.main()

