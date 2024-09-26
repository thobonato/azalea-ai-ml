import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_query_endpoint(self):
        response = self.client.post('/api/query', json={
            'query': 'Test query',
            'model': 'google'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('result', data)
        self.assertIn('score', data)
        self.assertIn('ecoMetrics', data)

# Add more tests as needed