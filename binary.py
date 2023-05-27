def decimal_to_binary(decimal):
    binary = ""
    if decimal == 0:
        binary = "0"
    else:
        while decimal > 0:
            binary = str(decimal % 2) + binary
            decimal = decimal // 2
    return binary

# Example usage
decimal_number = 42
binary_number = decimal_to_binary(decimal_number)
print("Binary representation:", binary_number)
