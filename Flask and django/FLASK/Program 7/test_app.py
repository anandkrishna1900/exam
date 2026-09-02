# test_app.py - automated tests using the Flask test client
import unittest
from app import app

class FlaskTests(unittest.TestCase):
    def setUp(self):
        # runs before each test: put the app in testing mode
        app.config['TESTING'] = True
        self.client = app.test_client()  # the test client

    def test_home(self):
        # check the home route returns 200 and the right text
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)

    def test_about(self):
        # check the about route
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'about page', response.data)

    def test_api_data(self):
        # check the JSON route returns the expected data
        response = self.client.get('/api/data')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'Sahan')
        self.assertEqual(data['course'], 'BCA')

    def test_square(self):
        # check the dynamic route computes correctly
        response = self.client.get('/square/5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['square'], 25)

    def test_not_found(self):
        # a URL with no route should return 404
        response = self.client.get('/no-such-page')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
