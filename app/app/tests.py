"""
Sample tests
"""
from django.test import SimpleTestCase # type: ignore

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numers(self):
        """Test adding numbers together"""
        res = calc.add(5,6)

        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        """Test subtracting numbers"""
        res = calc.subtract(10,15)

        self.assertEqual(res, 5)