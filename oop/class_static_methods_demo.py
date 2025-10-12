class Calculator:
    """A calculator class demonstrating the use of class methods and static methods."""
    
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """Static method that returns the sum of two numbers.
        
        Args:
            a: First number.
            b: Second number.
            
        Returns:
            The sum of a and b.
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """Class method that returns the product of two numbers.
        
        This method accesses the class attribute calculation_type and prints it
        before performing the multiplication.
        
        Args:
            cls: The class itself (automatically passed).
            a: First number.
            b: Second number.
            
        Returns:
            The product of a and b.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
