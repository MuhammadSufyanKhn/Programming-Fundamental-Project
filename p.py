def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return binary

def binary_to_decimal(binary):
    decimal = int(binary,2)
    return decimal

def decimal_to_octal(decimal):
    octal = oct(decimal)[2:]
    return octal

def octal_to_decimal(octal):
    decimal = int(octal,8)
    return decimal

def decimal_to_hexadecimal(decimal):
    hexadecimal = hex(decimal)[2:]
    return hexadecimal

def hexadecimal_to_decimal(hexadecimal):
    decimal = int(hexadecimal,16)
    return decimal

def hexadecimal_to_binary(hexadecimal):
    decimal = int(hexadecimal,16)
    binary = bin(decimal)[2:]
    return binary

while True:
    print('choose a conversion')
    print('1. Decimal to binary')
    print('2. Binary to decimal')
    print('3. Decimal to octal')
    print('4. Octal to decimal')
    print('5. Decimal to hexadecimal')
    print('6. Hexadecimal to decimal')
    print('7. Hexadecimal to binary')
    print('8. Quit the conversation')
    
    choice = int(input('Enter your choice between 1-8: '))
    
    if choice == 8:
        print("Conversion Ended!")
        break
    
    if choice not in [1 ,2 ,3 ,4 ,5 , 6, 7]:
        print('ERROR! number should be between 1-8')
        continue
    
    num = int(input('Enter a number to convert: '))
    
    if choice == 1:
        print(f'The binary representation of {num} is: {decimal_to_binary(int(num))}')
    elif choice == 2:
        print(f'The decimal representation of {num} is: {binary_to_decimal(str(num))}')
    elif choice == 3:
        print(f'The Octal representation of {num} is: {decimal_to_octal(int(num))}')
    elif choice == 4:
        print(f'The decimal representation of {num} is: {octal_to_decimal(str(num))}')
    elif choice == 5:
        print(f'The hexadecimal representation of {num} is: {decimal_to_hexadecimal(int(num))}')
    elif choice == 6:
        print(f'The decimal representation of {num} is: {hexadecimal_to_decimal(str(num))}')
    elif choice == 7:
        print(f'The binary representation of {num} is: {hexadecimal_to_binary(str(num))}')
    input("Press Enter to continue...")
    print()
