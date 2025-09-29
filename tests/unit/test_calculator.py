"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, divide, subtract, multiplication, division

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add(-2, -3) == -5
        assert add(-10, 5) == -5
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        assert subtract(-5, -3) == -2
        assert subtract(-10, 4) == -14

class TestMultiplyDivide:
    """Test multiplication and division operations"""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers"""
        assert multiplication(2, 3) == 6
        assert multiplication(10, 5) == 50
    
    def test_divide_positive_numbers(self):
        """Test dividing positive numbers"""
        assert division(6, 3) == 2
        assert division(10, 2) == 5

    def test_multiply_by_zero(self):
        """Test multiplying by zero"""
        assert multiplication(0, 5) == 0
        assert multiplication(10, 0) == 0
    
    def test_divide_by_one(self):
        """Test dividing by one"""
        assert division(5, 1) == 5
        assert division(10, 1) == 10

    def test_divide_by_zero(self):
        """Test dividing by zero raises ValueError"""
        with pytest.raises(ZeroDivisionError):
            division(5, 0)
        with pytest.raises(ZeroDivisionError):
            division(10, 0)

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)

# TODO: Students will add TestMultiplyDivide class