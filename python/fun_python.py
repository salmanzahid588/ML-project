def is_even(number):
    """
    this number will tell us this number is even or odd
    """
    if number%2==0:
        return'Even'
    else:
        return'Odd'
    
for i in range(1,11):
    print(is_even(i))
    
