class ExpressionSolver:
    def __init__(self, expression):
        self.expression = expression

    def solve(self):
        try:
            result = eval(self.expression)
            print("Expression:", self.expression)
            print("Result:", result)
        except Exception as e:
            print("Error while solving expression:", e)


expr1 = ExpressionSolver("10 + 20 * 3")
expr1.solve()

expr2 = ExpressionSolver("(50 - 20) / 3")
expr2.solve()
