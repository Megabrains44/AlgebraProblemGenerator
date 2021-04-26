Algebra generator that can easily create algebra equations in the Ax + b = C format. It can also solve equations in Ax + b = C. Right now, only the operations, '-' and '+' are supported

# Getting Started

You can install the module via pip:

`pip install algebraMathGenerator`

You can also clone the github like this:

`git clone https://github.com/Megabrains44/AlgebraProblemGenerator.git`

# Examples
The following is an example of how to create a algebra math equation. The `algebraMathGenerator.generateAlgebraEquation()` will return a class, so you can get the equation by adding a `.equation` after it.


```py
import algebraMathGenerator

equationClass = algebraMathGenerator.generateAlgebraEquation(operation = "+")
print(equationClass.equation) # returns equation 

```

You can solve equations with `algebraMathGenerator.solveAlgebraEquation(equation : class)`. The equation variable should be a class returned from `algebraMathGenerator.generateAlgebraEquation()`

```py
import algebraMathGenerator

equationClass = algebraMathGenerator.generateAlgebraEquation(operation = "+")
answer = algebraMathGenerator.solveAlgebraEquation(equationClass)
print(equationClass.equation) # returns an equation
print(answer) # returns the answer to the equation above

```



You can even loop through the generate method to produce a bunch of equations and their answers!


# Documentation
## Class `algebraMathGenerator`
2 functions
### Function: `.generateAlgebraEquation(operation : str)`
* > `.equation` - returns the equation Example: `2x + 4 = 6`
* > `.variable` - returns the variable Example: `x`
* > `.operation` - returns the operation done Example: `+`
* > `.equalsTo` - returns the number the equation is equal to. Example: `6`
* > `.coeffecient` - returns the number mutiplied by the variable Example: `2`
* > `.constant` - returns the constant term in the equation. Example: `4`

Returns `class` object

### Function: `.solveAlgebraEquation(equation : class)`
Input should be of type `.generateAlgebraEquation()`

Returns `float` value
