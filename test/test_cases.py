from code.finance_calc import *

def round_func(num):
	return round(num, 6)

def test_SI_pass():
	assert round_func(8000) == round_func(SimpleInterest(10000,8,10))
	
def test_SI_fail():
	assert round_func(8560) ==  round_func(SimpleInterest(10700,8,10))
	
def test_CI_pass():
	assert round_func(10088) == round_func(CompoundInterest(64000,5,3))
	
def test_CI_fail():
	assert "Principal negative, invalid input for function" ==  CompoundInterest(-9,8,10)
	
def test_inflation_pass():
	assert round_func(16288.94626777) == round_func(Inflation(10000,5,10))
	
def test_inflation_fail():
	assert "Time negative, invalid input for function" == Inflation(600,5,-3)
	
def test_purchasingPower_pass():
	assert round_func(6139.13253540) == round_func(PurchasingPower(10000,5,10))
	
def test_purchasingPower_fail():
	assert "Rate negative, invalid input for funtion" == PurchasingPower(64000,-5,3)
