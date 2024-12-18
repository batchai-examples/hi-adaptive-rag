import unittest

class TestConstants(unittest.TestCase):
    """
    Test suite for the Constants class.
    This suite includes tests for the DATETIME_FORMAT constant and 
    checks the immutability of the class attributes.
    """

    def test_datetime_format(self):
        """
        Test that the DATETIME_FORMAT constant is correctly defined.
        """
        # Check if the DATETIME_FORMAT is set to the expected format
        self.assertEqual(Constants.DATETIME_FORMAT, "%Y-%m-%d %H:%M:%S")

    def test_constant_immutability(self):
        """
        Test that attempting to set a new value to an existing constant raises an error.
        """
        # Attempt to set a new value to the DATETIME_FORMAT constant
        with self.assertRaises(RuntimeError):
            Constants.DATETIME_FORMAT = "%d-%m-%Y"

    def test_non_existent_constant(self):
        """
        Test that accessing a non-existent constant raises an AttributeError.
        """
        # Check that accessing a non-existent attribute raises an error
        with self.assertRaises(AttributeError):
            _ = Constants.NON_EXISTENT_CONSTANT

    def test_constant_type(self):
        """
        Test that the type of the DATETIME_FORMAT constant is a string.
        """
        # Ensure that the type of DATETIME_FORMAT is string
        self.assertIsInstance(Constants.DATETIME_FORMAT, str)

    def test_constant_value(self):
        """
        Test that the DATETIME_FORMAT constant has the correct value.
        """
        # Verify that the value of DATETIME_FORMAT is as expected
        self.assertEqual(Constants.DATETIME_FORMAT, "%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':
    unittest.main()
