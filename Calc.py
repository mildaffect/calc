def main(input: str):
    split_input_str = input.split()

    if len(split_input_str) != 3:
        return "throws Exception"

    try:
        first_operator = int(split_input_str[0])
        second_operator = int(split_input_str[2])
        operand = split_input_str[1]

    except ValueError:
        return "throws Exception"

    if not(1 <= first_operator <= 10 and 1 <= second_operator <= 10):
        return "throws Exception"


    if operand == '+':
        return str(first_operator + second_operator)
    elif operand == '-':
        return str(first_operator - second_operator)
    elif operand == '*':
        return str(first_operator * second_operator)
    elif operand == '/':
        return str(first_operator // second_operator)
    else:
        return "throws Exception"

while True:
    user_input = input("")
    result = main(user_input)

    print(result)