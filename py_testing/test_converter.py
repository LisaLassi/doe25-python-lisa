import pytest
from converter import celsius_to_fahrenheit, fahrenheit_to_celsius

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212

def test_fahrenheit_to_celsius(): 
    assert fahrenheit_to_celsius(32) == 0 
    assert round(fahrenheit_to_celsius(212)) == 100

    """
    Utöka gärna med: negativ temperatur
    test på flyttal
    test av rundning
    """