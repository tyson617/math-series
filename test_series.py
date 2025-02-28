import unittest  # Import the unittest module for writing test cases

# Attempt to import the series module, handling the case where it is missing
try:
    from series import fibonacci, lucas, sum_series  # Import functions to be tested
except ModuleNotFoundError:
    raise ImportError("The 'series' module is missing. Ensure that series.py exists in the same directory.")

class TestSeriesFunctions(unittest.TestCase):  # Define a test case class inheriting from unittest.TestCase
    
    def test_fibonacci(self):
        """Test the Fibonacci function with known values."""
        self.assertEqual(fibonacci(0), 0)  # Check base case
        self.assertEqual(fibonacci(1), 1)  # Check base case
        self.assertEqual(fibonacci(5), 5)  # Check known Fibonacci value
        self.assertEqual(fibonacci(10), 55)  # Check known Fibonacci value
        with self.assertRaises(ValueError):  # Ensure negative input raises an error
            fibonacci(-1)
    
    def test_lucas(self):
        """Test the Lucas function with known values."""
        self.assertEqual(lucas(0), 2)
        self.assertEqual(lucas(1), 1)
        self.assertEqual(lucas(5), 11)
        self.assertEqual(lucas(10), 123)
        with self.assertRaises(ValueError):
            lucas(-1)
    
    def test_sum_series_fibonacci(self):
        """Test sum_series function when used as Fibonacci series."""
        self.assertEqual(sum_series(0), 0) 
        self.assertEqual(sum_series(1), 1) 
        self.assertEqual(sum_series(5), 5) 
        self.assertEqual(sum_series(10), 55) 
    
    def test_sum_series_lucas(self):
        """Test sum_series function when used as Lucas series."""
        self.assertEqual(sum_series(0, 2, 1), 2)  
        self.assertEqual(sum_series(1, 2, 1), 1)  
        self.assertEqual(sum_series(5, 2, 1), 11) 
        self.assertEqual(sum_series(10, 2, 1), 123) 
    
    def test_sum_series_custom(self):
        """Test sum_series function with custom initial values."""
        self.assertEqual(sum_series(0, 3, 4), 3)  
        self.assertEqual(sum_series(1, 3, 4), 4)
        self.assertEqual(sum_series(5, 3, 4), 29) 
        self.assertEqual(sum_series(10, 3, 4), 322) 
        with self.assertRaises(ValueError): 
            sum_series(-1, 3, 4)

if __name__ == '__main__':  # Standard Python boilerplate to run tests when script is executed directly
    unittest.main()
