def Calc(value1, value2, calcOperator):
    v1 = float(value1)
    v2 = float(value1)
    
    
   
    returnValue = 0;
    
    if calcOperator == "add":
        returnValue = v1 + v2;
    elif calcOperator == "Subtract":
        returnValue = v1 - v2;
    elif calcOperator == "Divide":
        returnValue = v1 / v2;
    elif calcOperator == "Multiply":
        returnValue = v1 * v2;
        
    return returnValue

obj = Calc(1, 1, 'add' )

print(obj)