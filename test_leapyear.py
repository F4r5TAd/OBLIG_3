
import pytest
from leapyear import isLeapYear

#Skuddårstester:
def test_year_divisible_by_4_but_not_100():
    assert isLeapYear(2004) == True, "Expected year 2004 to be a leap year."
    assert isLeapYear(2008) == True, "Expected year 2008 to be a leap year."
    assert isLeapYear(2012) == True, "Expected year 2008 to be a leap year."
    assert isLeapYear(2016) == True, "Expected year 2008 to be a leap year."
    assert isLeapYear(2020) == True, "Expected year 2008 to be a leap year."
    assert isLeapYear(2028) == True, "Expected year 2008 to be a leap year."

def test_year_divisible_by_400():
    assert isLeapYear(2000) == True, "Expected year 2000 to be a leap year."
    assert isLeapYear(2400) == True, "Expected year 2400 to be a leap year."
    assert isLeapYear(2800) == True, "Expected year 2000 to be a leap year."
    assert isLeapYear(3200) == True, "Expected year 2000 to be a leap year."
#Ikke skuddårstester:
def test_year_not_divisible_by_4():
    assert isLeapYear(2001) == False, "Expected year 2001 to not be a leap year."
    assert isLeapYear(2002) == False, "Expected year 2002 to not be a leap year."
    assert isLeapYear(2003) == False, "Expected year 1990 to not be a leap year."
    assert isLeapYear(2005) == False, "Expected year 1990 to not be a leap year."
    assert isLeapYear(2006) == False, "Expected year 1990 to not be a leap year."
    assert isLeapYear(1990) == False, "Expected year 1990 to not be a leap year."

def test_year_divisible_by_100_but_not_400():
    assert isLeapYear(1700) == False, "Expected year 1700 to not be a leap year."
    assert isLeapYear(1800) == False, "Expected year 1800 to not be a leap year."
    assert isLeapYear(1900) == False, "Expected year 1900 to not be a leap year."
    assert isLeapYear(2100) == False, "Expected year 2100 to not be a leap year."
    assert isLeapYear(2200) == False, "Expected year 2100 to not be a leap year."
    assert isLeapYear(2300) == False, "Expected year 2100 to not be a leap year."