#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        - data: List of integers representing the data set

    Returns:
        - True if data is a valid UTF-8 encoding, else False
    """
    num_bytes_to_follow = 0

    for num in data:
        if num_bytes_to_follow > 0 and (num >> 6) == 2:
            num_bytes_to_follow -= 1
        elif num_bytes_to_follow == 0:
            if (num >> 7) == 0b0:
                num_bytes_to_follow = 0
            elif (num >> 5) == 0b110:
                num_bytes_to_follow = 1
            elif (num >> 4) == 0b1110:
                num_bytes_to_follow = 2
            elif (num >> 3) == 0b11110:
                num_bytes_to_follow = 3
            else:
                return False
        else:
            return False

    return num_bytes_to_follow == 0


# Entry point for testing
if __name__ == '__main__':
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))

