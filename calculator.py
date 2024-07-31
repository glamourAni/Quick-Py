class Calculator:
    operators = ('^', '*', '/', '%', '+', '-')
    stack = []
    top = -1

    def __init__(self, infix):
        self.infix = infix
    
    def float_isnum(self, s):
        if s.replace(".", "").isnumeric():
            return True
        return False

    # convert number values to their unique number types
    def getType(self, n: str) -> int | float:
        if self.float_isnum(n):
            n = float(n)
            if n.is_integer():
                n = int(n)
        return n

    # define hierarchy of operators
    def precedence(self, op):
        if op == '^': 
            return 3
        elif op == '*' or op == '/' or op == '%':
            return 2
        elif op == '+' or op == '-':
            return 1
        else:
            return -1

    def calculate(self, a, op, b):
        if op == '^': return a**b
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/':
            res = a / b
            if res.is_integer(): 
                return int(res)
            else:
                return res
        return None

    def percent(self, a):
        return a / 100

    def _pop(self):
        last = Calculator.stack.pop()
        Calculator.top -= 1
        return last
        

    def push(self, x):
        Calculator.stack.append(x)
        Calculator.top += 1
        

    def infixToPostfix(self):
        # first convert the infix expression to a list to accurately retrieve number values
        exprArr = []
        num = ""
        for i in self.infix:
            if i.isdigit() or i == ".":
                num += i
            else:
                exprArr.append(num)
                exprArr.append(i)
                num = ""
        exprArr.append(num) #adds the last number
        exprArr = filter(lambda item: item.strip(), exprArr)
        postfix_expr = []

        for character in exprArr:
            if character in Calculator.operators:
                    #check the precedence of the evaluated operator and the operator in stack 
                    if Calculator.stack != [] and self.precedence(Calculator.stack[Calculator.top]) >= self.precedence(character):
                        postfix_expr.append(self._pop()) #adds the last operator in stack to postfix_expr if it is less in precedence to the operator being evaluated 
                    self.push(character) #adds operator to stack
            elif character == '(' or character == '[':
                self.push(character)
            elif character == ')' or character == ']':
                if character == ')':
                    while not Calculator.stack[Calculator.top] == '(':        
                        postfix_expr.append(self._pop())
                    self._pop()
                if character == ']':
                    while not Calculator.stack[Calculator.top] == '[':
                        postfix_expr.append(self._pop())
                    self._pop()
            else:
                postfix_expr.append(self.getType(character))
        while Calculator.stack != []:
            postfix_expr.append(self._pop())

        return postfix_expr

    def evaluatePostfix(self):
        postfix = self.infixToPostfix()
        result = 0
        self.push(0)

        for val in postfix:
            try:
                if Calculator.stack != [] and val in Calculator.operators:
                    num1 = Calculator.stack[Calculator.top - 1]
                    num2 = Calculator.stack[Calculator.top]
                    if val == "%":
                        result = self.percent(num2)
                    else:
                        result = self.calculate(num1, val, num2)
                    # pop the last two numbers and add the result to the top of the stack
                    self._pop()
                    self._pop()
                    self.push(result)
                elif val not in Calculator.operators:
                    if len(postfix) == 1: result = val
                    self.push(val)
                else:
                    return 0 # if the expression contains only operators
            except:
                raise

        while Calculator.stack != []:
            self._pop()

        return result

while True:
    expression = input("Enter an expression you want to calculate(Hit the 'Enter' key to quit): ")
    if expression == "":
        break
    else:
        newCalculator = Calculator(expression)
        print(f"Result: {newCalculator.evaluatePostfix()}\n")
