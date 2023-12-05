import re


digit_names = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}


def convert_digit_names(values):
    converted_values = []
    for value in values:
        for name in digit_names.keys():
            value = re.sub(name, name[0] + digit_names[name] + name[-1], value)
        converted_values.append(value)

    return converted_values


def calculate_calibration(values):
    sum = 0
    for value in values:
        digits = re.sub(r'\D', '', value)
        if len(digits) == 1:
            digits += digits[0]
        if len(digits) > 2:
            digits = digits[0] + digits[-1]
        sum += int(digits)

    return sum


def main():
    f = open('calibration_doc.txt', 'r')
    values = f.readlines()

    sum = calculate_calibration(values)
    print('Sum of part 1 calibration values:', sum)

    converted_values = convert_digit_names(values)
    converted_sum = calculate_calibration(converted_values)
    print('Sum of part 2 calibration values:', converted_sum)


main()