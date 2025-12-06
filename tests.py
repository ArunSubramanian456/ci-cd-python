import unittest 
import app

class BasicTestCase(unittest.TestCase):
    def test_home(self):
        tester = app.app.test_client()
        response = tester.get('/', content_type='text/html')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello', response.data) 
        print(response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
