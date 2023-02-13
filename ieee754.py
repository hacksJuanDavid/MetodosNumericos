import struct # Import struct library 

# Function to convert decimal to binary
def decimal_to_bin(num, precision):
    if precision == "simple":
        bin_num = format(struct.unpack('!I', struct.pack('!f', num))[0], 'b').zfill(32)
        sign = bin_num[0]
        exponent = bin_num[1:9]
        mantissa = bin_num[9:]
        decimal_exponent = int(exponent, 2) - 127
        decimal_mantissa = int(mantissa, 2) / 2**23
        decimal_mantissa_str = str(decimal_mantissa)[2:18]
        decimal_equivalent = (-1)**int(sign) * (1 + decimal_mantissa) * 2**decimal_exponent
        return (sign, exponent, mantissa, decimal_exponent, decimal_mantissa, decimal_mantissa_str, decimal_equivalent)
    elif precision == "doble":
        bin_num = format(struct.unpack('!Q', struct.pack('!d', num))[0], 'b').zfill(64)
        sign = bin_num[0]
        exponent = bin_num[1:12]
        mantissa = bin_num[12:]
        decimal_exponent = int(exponent, 2) - 1023
        decimal_mantissa = int(mantissa, 2) / 2**52
        decimal_mantissa_str = str(decimal_mantissa)[2:18]
        decimal_equivalent = (-1)**int(sign) * (1 + decimal_mantissa) * 2**decimal_exponent
        return (sign, exponent, mantissa, decimal_exponent, decimal_mantissa, decimal_mantissa_str, decimal_equivalent)

# Function to convert decimal to hexadecimal
def decimal_to_hex(num, precision):
    if precision == "simple":
        return format(struct.unpack('!I', struct.pack('!f', num))[0], 'x')
    elif precision == "doble":
        return format(struct.unpack('!Q', struct.pack('!d', num))[0], 'x')

# Function to main
def main():
    num = float(input("Introduce un número decimal: "))

    print("Simple Precision:")
    (sign, exponent, mantissa, decimal_exponent, decimal_mantissa, decimal_mantissa_str, decimal_equivalent) = decimal_to_bin(num, "simple")
    hex_simple = decimal_to_hex(num, "simple")
    print(f"Signo: {sign}")
    print(f"Exponente: {exponent} (decimal: {decimal_exponent})")
    print(f"Mantissa: {mantissa} (decimal: {decimal_mantissa_str})")
    print(f"Valor decimal equivalente: {decimal_equivalent}")
    print(f"Binario: {sign}{exponent}{mantissa}")
    print(f"Hexadecimal: {hex_simple}")

    print("Doble Precision:")
    (sign, exponent, mantissa, decimal_exponent, decimal_mantissa, decimal_mantissa_str, decimal_equivalent) = decimal_to_bin(num, "doble")
    hex_doble = decimal_to_hex(num, "doble")
    print(f"Signo: {sign}")
    print(f"Exponente: {exponent} (decimal: {decimal_exponent})")
    print(f"Mantissa: {mantissa} (decimal: {decimal_mantissa_str})")
    print(f"Valor decimal equivalente: {decimal_equivalent}")
    print(f"Binario: {sign}{exponent}{mantissa}")
    print(f"Hexadecimal: {hex_doble}")

if __name__ == "__main__":
    main()
