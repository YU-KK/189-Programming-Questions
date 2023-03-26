#順列チェック
#2つの文字列が与えられた時、片方がもう片方の並び替えになっているかどうかを決定するもそっどを書いてください。

def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    str1_count = {}
    for char in str1:
        if char in str1_count:
            str1_count[char] += 1
        else:
            str1_count[char] = 1

    for char in str2:
        if char in str1_count:
            str1_count[char] -= 1
            if str1_count[char] < 0:
                return False
        else:
            return False

    return True

# 使用例
str1 = "abcde"
str2 = "edcba"
result = is_permutation(str1, str2)
print(result)  # Trueを返す

str3 = "abcde"
str4 = "edcfg"
result2 = is_permutation(str3, str4)
print(result2)  # Falseを返す
