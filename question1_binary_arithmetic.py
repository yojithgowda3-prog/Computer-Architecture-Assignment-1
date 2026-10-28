
def to_8bit(value):
    """Return the 8-bit two's complement representation."""
    return format(value & 0xFF, "08b")


def binary_arithmetic(a, b):
    # Calculate a - b using 8-bit two's complement.
    a_bits = to_8bit(a)
    b_bits = to_8bit(b)
    negative_b_bits = to_8bit(-b)

    result_unsigned = (a + (-b)) & 0xFF
    result_bits = format(result_unsigned, "08b")

    # Interpret the 8-bit result as a signed integer.
    result_decimal = (
        result_unsigned - 256
        if result_unsigned >= 128
        else result_unsigned
    )

    # Signed overflow occurs when the mathematical result
    # lies outside the signed 8-bit range.
    mathematical_result = a - b
    overflow = not (-128 <= mathematical_result <= 127)

    print("\nExpression:", f"({a}) - ({b})")
    print("First operand:       ", a_bits)
    print("Second operand:      ", b_bits)
    print("2's complement of B: ", negative_b_bits)
    print("Binary result:       ", result_bits)
    print("Decimal result:      ", result_decimal)
    print("Overflow:            ", "Yes" if overflow else "No")


binary_arithmetic(45, 19)
binary_arithmetic(-35, -12)
