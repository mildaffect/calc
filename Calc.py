def main(input: str):
    split_input_str = input.split()

    if len(split_input_str) != 3:
        return "throws Exception"

    try:
        first_operand = int(split_input_str[0])
        second_operand = int(split_input_str[2])
        operator = split_input_str[1]

    except ValueError:
        return "throws Exception"

    if not(1 <= first_operand <= 10 and 1 <= second_operand <= 10):
        return "throws Exception"


    if operator == '+':
        return str(first_operand + second_operand)
    elif operator == '-':
        return str(first_operand - second_operand)
    elif operator == '*':
        return str(first_operand * second_operand)
    elif operator == '/':
        return str(first_operand // second_operand)
    else:
        return "throws Exception"

while True:
    user_input = input("")
    result = main(user_input)

    print(result)