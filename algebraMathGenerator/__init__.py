import random
    
        

def generateAlgebraEquation(operation=None):
    if operation == None:
        operation = random.choice(['+','-'])
    if operation not in  ['+','-']:
        raise ValueError("Invalid operation type. Only + and - are currently supported")
    
    variable = random.choice(["x","y","z","a","b","c","d","f"])
    coeffecient = random.randint(1,10)
    constant = random.randint(1,10)
    equalsTo = random.randint(5,100)
    
    
    
    
        
    equation = str(coeffecient) + str(variable) + " " + str(operation) +" "+ str(constant) + " = " + str(equalsTo)
    class Information():
        def __init__(self):
            self.equation = equation
            self.coeffecient = coeffecient
            self.variable = variable
            self.operation = operation
            self.constant = constant
            self.equalsTo = equalsTo
    return Information()
    
    
    

   
        
    





def solveAlgebraEquation(algGenerator):
    
    
    equation = algGenerator.equation
    coeffecient = algGenerator.coeffecient
    variable = algGenerator.variable
    operation = algGenerator.operation
    constant = algGenerator.constant
    equationEqualTo = algGenerator.equalsTo
    
    if operation == '+':
        
        variable = (equationEqualTo - constant)/coeffecient
    elif operation == '-':
        variable = (equationEqualTo - constant)/coeffecient
    else:
        raise ValueError(f"Cannot parse '{equation}' as an operator. Only '+' and '-' are valid.")
    return variable
    





