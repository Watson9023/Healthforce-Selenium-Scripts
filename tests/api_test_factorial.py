import unittest
import requests


class TestFactorialAPI(unittest.TestCase):

    def test_factorial_calculation(self):
        url = "http://localhost:6464/factorial"
        payload = {"number": 7}
        response = requests.post(url, json=payload)

        self.assertEqual(response.status_code, 200, "API call failed")

        data = response.json()
        calculated_result = data.get("answer")
        expected_result = 5040
        self.assertEqual(calculated_result, expected_result, "Unexpected result")


if __name__ == "__main__":
    unittest.main()
