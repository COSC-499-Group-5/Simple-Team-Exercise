def factorial(number):
    # initilize hash map
    dpArray = {}
    # if number is in hash map, return the factorial version of that number
    if number in dpArray:
        return dpArray[number]
    
    # Cannot take factorial of negative number
    if number <= -1:
        return "cannot take factorial of a negative number"
    
    # base case 0! = 1
    if number == 0 or number == 1:
        return 1
    
    # else call recursive 
    fact = number * factorial(number - 1)
    dpArray[number] = fact
    return fact

