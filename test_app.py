# test_app.py
import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_route_0(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_hello_route_1(self):
        response = self.app.get('/')
        self.assertNotEqual(response.data.decode('utf-8'), 'Hello, World!')

    def test_home_route_0(self):
        response = self.app.get('/home')
        self.assertEqual(response.status_code, 200)
        
    def test_hello_route_1(self):
        response = self.app.get('/home', follow_redirects=True)
        self.assertIn(b'Welcome to My Home Page', response.data)


if __name__ == '__main__':
    unittest.main()
