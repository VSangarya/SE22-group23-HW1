"""
A simple interest calculator method.
Returns the final principal amount
"""
def SimpleInterest(principal, rate, time):
  if principal < 0: return "Principal negative, invalid input for function"
  if rate < 0: return "Rate negative, invalid input for funtion"
  if time < 0: return "Time negative, invalid input for function"
  return (principal*rate*time)/100

def CompoundInterest(principal, rate, time):
  if principal < 0: return "Principal negative, invalid input for function"
  if rate < 0: return "Rate negative, invalid input for funtion"
  if time < 0: return "Time negative, invalid input for function"
  return (principal*((1+(rate/100))**time)) - principal

def Inflation(principal, rate, time):
  if principal < 0: return "Principal negative, invalid input for function"
  if rate < 0: return "Rate negative, invalid input for funtion"
  if time < 0: return "Time negative, invalid input for function"
  return principal*((1+(rate/100))**time)

def PurchasingPower(principal, rate, time):
  if principal < 0: return "Principal negative, invalid input for function"
  if rate < 0: return "Rate negative, invalid input for funtion"
  if time < 0: return "Time negative, invalid input for function"
  return principal/(((1+(rate/100))**time))
