from addminus import *
from factorial import *
from gcd import *
from lcm import *
from minmax import *
from multipy import *

#addminus.py
def addTest():
    param1 = 5
    param2 = 10
    assert add(param1,param2) == 15, "Should be 15"

def minusTest():
    param1 = 20
    param2 = 10
    assert minus(param1,param2) == 10, "Should be 10"

#multipy.py
def multTest():
    param1 = 20
    param2 = 10
    assert multiply(param1,param2) == 200, "Should be 200"

#factorial.py
def factorialTest():
    param1 = 5
    assert factorial(param1) == 120, "Should be 120"

#gcd.py
def gcdTest():
    param1 = 5
    param2 = 10
    assert gcd.gcd(param1, param2) == 5, "Should be 5"

#lcm.py
def lcmTest():
    param1 = 5
    param2 = 10
    assert lcm(param1, param2) == 10, "Should be 10"

#minmax.py
def minTest():
    param1 = 5
    param2 = 10
    assert min(param1, param2) == 5, "Should be 5"

def maxTest():
    param1 = 5
    param2 = 10
    assert max(param1, param2) == 10, "Should be 10"
        
if __name__ == "__main__":
    addTest()
    minusTest()
    factorialTest()
    multTest()
    gcdTest()
    lcmTest()
    minTest()
    maxTest()
    print("Everything passed") 