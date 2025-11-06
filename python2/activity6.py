class ExpressionSolver:
    def __init__(self, expression):
        self.expression = expression  # store the expression

    def solve(self):
        try:
            result = eval(self.expression)  # evaluate the expression
            return result
        except Exception as t:
            return f"Error:" {}

    def display_result(self):
        result = self.solve()
        print(f"The result of '{self.expression}' is: {result}")


