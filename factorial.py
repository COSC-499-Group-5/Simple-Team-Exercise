def factorial(number):
    # Cannot take factorial of negative number
    if number <= -1:
        return "cannot take factorial of a negative number"
    
    # base case 0! = 1
    if number == 0:
        return 1
    
    # else call recursive 
    return number * factorial(number - 1)

    
