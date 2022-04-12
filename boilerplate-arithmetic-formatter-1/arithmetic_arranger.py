'''
["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]

  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
'''


def arithmetic_arranger(problems: list, second_argument: bool):

    first_line = []
    second_line = []
    third_line = []
    results = []

    for operation in problems:
        first, opera, second = operation.split(" ")
        
        first_line.append(first)
        second_line.append(opera + " " + second)

        result = calculate(first, second, opera)
        results.append(result)

        maximum = max(len(first), len(second) + 2, len(str(result)))
        third_line.append(maximum * "-")

        
    data = [first_line, second_line, third_line, results]
    arranged_problems = ""
    # print(data)
    for i in range(4):
        finall = f"{data[i][0]:>5}    {data[i][1]:>5}   {data[i][2]:>5}    {data[i][3]:>5}\n"
        arranged_problems += finall
        
    return arranged_problems

            

def calculate(num1:int, num2:int, symbol:str):
    if symbol == "+":
        return int(num1) + int(num2)
    elif symbol == "-":
        return int(num1) - int(num2)
    elif symbol == "*":
        return int(num1) * int(num2)
    elif symbol == "/":
        return int(num1) / int(num2)
    
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))