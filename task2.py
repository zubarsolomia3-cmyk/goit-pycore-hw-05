import re 


def generator_numbers(text: str):
    """
    Генератор, який знаходить усі дійсні числа у тексті
    і поступово повертає їх (yield).
    """

   
    numbers = re.findall(r"\d+\.\d+|\d+", text)

    for number in numbers:
        yield float(number)  


def sum_profit(text: str, func):
    """
    Використовує generator_numbers для підсумовування
    всіх чисел у тексті.
    """
    total = sum(func(text))  
    return total



text = (
    "Загальний дохід працівника складається з декількох частин: "
    "1000.01 як основний дохід, доповнений додатковими надходженнями "
    "27.45 і 324.00 доларів."
)

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
