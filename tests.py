import unittest
from app import app


class DeviceSetupTests(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_title(self):
        response = self.client.get("/")
        self.assertIn(b"Ubuntu Core Device Setup", response.data)

    def test_setup_flow_exists(self):
        response = self.client.get("/")
        self.assertIn(b"Device Setup Flow", response.data)
        self.assertIn(b"Device Status", response.data)


if __name__ == "__main__":
    unittest.main()