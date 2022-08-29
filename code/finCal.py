"""
A simple interest calculator method.
Returns the final principal amount
"""
def simpleInterest(principal, rate, time):
	if(principal < 0): return "Principal negative, invalid input for function"
	if(rate < 0): return "Rate negative, invalid input for funtion"
	if(time < 0): return "Time negative, invalid input for function"
	return (principal*rate*time)/100

def compoundInterest(principal, rate, time):
    if(principal < 0): return "Principal negative, invalid input for function"
	if(rate < 0): return "Rate negative, invalid input for funtion"
	if(time < 0): return "Time negative, invalid input for function"
	return (principal*((1+(rate/100))**time)) - principal

def inflation(principal, rate, time):
    if(principal < 0): return "Principal negative, invalid input for function"
	if(rate < 0): return "Rate negative, invalid input for funtion"
	if(time < 0): return "Time negative, invalid input for function"
	return principal*((1+(rate/100))**time)

def purchasingPower(principal, rate, time):
    if(principal < 0): return "Principal negative, invalid input for function"
	if(rate < 0): return "Rate negative, invalid input for funtion"
	if(time < 0): return "Time negative, invalid input for function"
	return principal/(((1+(rate/100))**time))