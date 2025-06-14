class CalculatorTool:
    name = "calculator"
    description = "Performs basic math operations"

    def run(self, expression: str) -> str:
        try:
            result = eval(expression)
            return f"The result of {expression} is {result}"
        except Exception as e:
            return f"Error: {str(e)}"
