def safe_calculate(func):
    def wrapper(expression):
        try:
            result = func(expression)
            return result
        except Exception as e:
            return f"Error: {e}"

    return wrapper

@safe_calculate
def calculate(expression):
    return eval(expression)

result = calculate("2 + 2")
print(result)  # Вывод: 4

result = calculate("10 / 0")
print(result)  # Вывод: Error: division by zero
