def is_unique_chars_no_data_structure(string):
    checker = 0

    for char in string:
        val = ord(char) - ord('a')
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)

    return True


test_string = "abcdefgh"
print(is_unique_chars_no_data_structure(test_string))  # True

test_string = "abcdeafgh"
print(is_unique_chars_no_data_structure(test_string))  # False
