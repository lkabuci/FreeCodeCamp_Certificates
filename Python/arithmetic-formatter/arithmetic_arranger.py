def arithmetic_arranger(problems: list, show_results: bool = False):

    if check_problems(problems) == True:
        first_line, second_line, third_line, results = "", "", "", ""

        for operation in problems:
            first, opera, second = operation.split()
            result = calculate(first, second, opera)

            diff = len(first) - len(second)
            if diff > 0:
                dashes = len(first) + 2
                first_line += f"  {first}    "
                second_line += f"{opera} {diff * ' '}{second}    "
                third_line += f"{dashes * '-'}    "
                results += f"{(dashes - len(str(result)))*' '}{result}    "
                
            elif diff < 0:
                dashes = len(second) + 2
                first_line += f"  {abs(diff) * ' '}{first}    "
                second_line += f"{opera} {second}    "
                third_line += f"{dashes * '-'}    "
                results += f"{(dashes - len(str(result)))*' '}{result}    "

            else:
                dashes = len(first) + 2
                first_line += f"  {first}    "
                second_line += f"{opera} {second}    "
                third_line += f"{dashes * '-'}    "
                results += f"{(dashes - len(str(result)))*' '}{result}    "

        first_line = first_line[:-4]
        second_line = second_line[:-4]
        third_line = third_line[:-4]
        results = results[:-4]

        if show_results == True:
            return f"{first_line}\n{second_line}\n{third_line}\n{results}"

        else:
            solution = f"{first_line}\n{second_line}\n{third_line}"

        return solution
    else:
        return check_problems(problems)


def check_problems(liste: list):
    if len(liste) > 5:
        return ("Error: Too many problems.")
    for operation in liste:
        single = operation.split(" ")
        first, second, third = single
        if is_integer(first) and is_integer(third):
            for item in single:
                if second == "/" or second == "*":
                    return ("Error: Operator must be '+' or '-'.")
                elif len(item) > 4:
                    return ("Error: Numbers cannot be more than four digits.")
        else:
            return "Error: Numbers must only contain digits."
    else:
        return True


def calculate(num1: int, num2: int, symbol: str):
    if symbol == "+":
        return int(num1) + int(num2)
    elif symbol == "-":
        return int(num1) - int(num2)


def is_integer(number):
    try:
        int(number)
    except ValueError:
        return False
    else:
        return True
