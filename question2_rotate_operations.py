
def rotate_left_without_carry(binary, positions):
    value = int(binary, 2)
    mask = 0xFF

    print("\nROL - Rotate Left Without Carry")
    print("Original number:", binary)

    for step in range(1, positions + 1):
        msb = (value >> 7) & 1
        value = ((value << 1) & mask) | msb
        print(f"After rotation {step}: {value:08b}")

    print("Final ROL result:", format(value, "08b"))


def rotate_left_with_carry(binary, positions, carry=0):
    value = int(binary, 2)
    mask = 0xFF

    print("\nRCL - Rotate Left With Carry")
    print("Original number:", binary)
    print("Initial carry:", carry)

    for step in range(1, positions + 1):
        new_carry = (value >> 7) & 1
        value = ((value << 1) & mask) | carry
        carry = new_carry

        print(
            f"After rotation {step}: "
            f"Carry = {carry}, Number = {value:08b}"
        )

    print("Final RCL result:", format(value, "08b"))
    print("Final carry:", carry)


number = "10110110"

rotate_left_without_carry(number, 2)
rotate_left_with_carry(number, 2, carry=0)
