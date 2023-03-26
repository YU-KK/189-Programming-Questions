#重複のない文字列
#ある文字列が、全て固有である（重複する文字がない）かどうかを判別するアルゴリズムを実装してください。
#また、それを実装するのに新たなデータ構造が使えない場合、どのようにすればよいですか？

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

