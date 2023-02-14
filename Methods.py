my_number = input("Type a number:")


def ConvertToDecimal(input):
    if (int(input[0]) > 0) and input.isnumeric():
        return int(input)
    elif (int(input[0]) == 0) and input.isnumeric():
        values = []
        for i in range(1, len(input) + 1):
            cur_value = int((input[i - 1])) * (8 ** (len(input) - i))
            values.append(cur_value)
        octal = 0
        for value in values:
            octal += value
        return octal
    elif input[:2] == "0x":
        my_input = input[2:]
        conversion_table = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "A": 10,
            "B": 11,
            "C": 12,
            "D": 13,
            "E": 14,
            "F": 15,
        }
        values = []
        for i in range(1, len(my_input) + 1):
            cur_value = conversion_table[my_input[i - 1]] * (16 ** (len(my_input) - i))
            values.append(cur_value)
        hexadecimal = 0
        for value in values:
            hexadecimal += value
        return hexadecimal
    elif int(input[0]) >= 1 and input.count(".") == 1:
        return input.split(".")
    else:
        return None


def decimal_to_binary(number):
    my_number = int(number)
    binary = ""
    while my_number > 0:
        cur_number = my_number % 2
        binary += str(cur_number)
        my_number = my_number // 2
    return binary[::-1]


def decimal_to_octal(number):
    octal = 0
    ctr = 0
    temp = int(number)  # copying number
    # computing octal using while loop
    while temp > 0:
        octal += (temp % 8) * (10**ctr)  # Stacking remainders
        temp = int(temp / 8)  # updating dividend
        ctr += 1

    return octal


# function which converts decimal value
# to hexadecimal value
def decimalToHexadecimal(decimal):
    decimal = int(decimal)
    conversion_table = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
    }
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16

    return hexadecimal


my_return = ConvertToDecimal(my_number)
print(my_return)
if isinstance(my_return, int):
    print("In decimal: " + str(my_return))
    print("In binary: " + decimal_to_binary(my_return))
    print("In octal: 0" + str(decimal_to_octal(my_return)))
    print("In hex: 0x" + decimalToHexadecimal(my_return))
elif isinstance(my_return, list):
    print("In decimal: " + my_return[0] + "." + my_return[1])
    print(
        "In binary: "
        + decimal_to_binary(my_return[0])
        + "."
        + decimal_to_binary(my_return[1])
    )
    print(
        "In octal: 0"
        + str(decimal_to_octal(my_return[0]))
        + "."
        + str(decimal_to_octal(my_return[1]))
    )
    print(
        "In hex: 0x"
        + decimalToHexadecimal(my_return[0])
        + "."
        + decimalToHexadecimal(my_return[1])
    )
elif isinstance(my_return, None):
    print("You entered an invalid number")
