
#The 'fizzbuzz' function definition
def fizz_buzz(inp):
    """
    This is a simple programme to test if a number is factor of 3 or 5
    or both.
    
    When a number that is a factor of 3 is inputted, the text 'FIZZ' is 
    returned. A factor of 5 will return the text 'BUZZ'.
    
    A factor of both numbers will return 'FIZZBUZZ'.
    
    A number that does not fulfil any of the above conditions will 
    return itself.

    Args:
        input (int): The number to be inputted must be an interger.
    """
    if (inp % 3 == 0) and (inp % 5 == 0):
        return('FIZZBUZZ')
        
    if inp % 3 == 0:
        return('FIZZ')
        
    if inp % 5 == 0:
        return('BUZZ')
        
    return(inp)
        
        

#The function call and printing the output
print(fizz_buzz(8))

