import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)
        
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        
        # Test with zero
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(7, 0), 7)
        self.assertEqual(self.calc.add(0, 0), 0)
        
        # Test floating point numbers
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)

    def test_subtraction(self):
        """Test the subtraction method."""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(5, 2), 3)
        
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(5, -3), 8)
        
        # Test with zero
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        
        # Test floating point numbers
        self.assertEqual(self.calc.subtract(5.5, 2.3), 3.2)

    def test_multiplication(self):
        """Test the multiplication method."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(2, 5), 10)
        
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-4, -3), 12)
        
        # Test with zero
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        
        # Test with one
        self.assertEqual(self.calc.multiply(7, 1), 7)
        self.assertEqual(self.calc.multiply(1, 9), 9)
        
        # Test floating point numbers
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)

    def test_division(self):
        """Test the division method."""
        # Test normal division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        
        # Test negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-12, -3), 4.0)
        
        # Test division by zero (should return None)
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        
        # Test zero dividend
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -3), 0.0)
        
        # Test floating point division
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertEqual(self.calc.divide(1, 3), 1/3)

if __name__ == "__main__":
    unittest.main()
