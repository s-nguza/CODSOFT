import unittest
from unittest.mock import patch
import password as password_generator

class TestPasswordGenerator(unittest.TestCase):
    @patch('builtins.input', side_effect=['5'])
    def test_user_input_valid(self, mock_input):
        result = password_generator.user_input()
        self.assertEqual(result, 5)

    
    def test_password_creation(self):
        password = password_generator.password_creation(8)
        self.assertEqual(len(password), 8)

if __name__ == '__main__':
    unittest.main()

