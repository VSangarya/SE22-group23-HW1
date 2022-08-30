from code.finance_calc import *

def test_SI_pass():
    assert 8000 == SimpleInterest(10000,8,10)
	
def test_SI_fail():
	assert 500 ==  SimpleInterest(10700,8,10)
	
def test_CI_pass():
    assert 74088 == CompoundInterest(64000,5,3)
	
def test_CI_fail():
	assert "Principal negative, invalid input for function" ==  CompoundInterest(-9,8,10)
	
def test_inflation_pass():
    assert 16289 == Inflation(10000,5,10)
	
def test_inflation_fail():
    assert "Time negative, invalid input for function" == Inflation(600,5,-3)
	
def test_purchasingPower_pass():
    assert 6139 == PurchasingPower(10000,5,10)
	
def test_purchasingPower_fail():
    assert "Rate negative, invalid input for funtion" == PurchasingPower(64000,-5,3)