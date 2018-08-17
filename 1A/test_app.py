import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] =True
        self.app=app.test_client()

    def tearDown(self):
        pass

    def test_api_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)


    #def test_api_post(self):
       # response = self.app.post('/', content_type='application/json')
        #self.assertEqual(response.status_code, 200)

    def test_api_delete(self):
        response = self.app.delete('/delete/5b7582c8f382632970f2f4c2')
        self.assertEqual(response.status_code, 200)

    def test_api_update(self):
        response = self.app.put('/update/5b7582c8f382632970f2f4c2')
        self.assertEqual(response.status_code, 200)

if __name__=="__main__":
    unittest.main()