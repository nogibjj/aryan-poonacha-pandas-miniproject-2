import unittest
from ids_706_python_template.cli import test  # Import the function you want to test

#example of a test
class TestTest(unittest.TestCase):
    def test_some_function(self):
        # Write test cases for some_function_to_test here
        result = test()  # Call the function you want to test
        self.assertEqual(result, 'test')  # Add assertions to check the expected result