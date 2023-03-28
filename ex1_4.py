def is_palindrome_permutation(s: str) -> bool:
    s = s.lower()
    char_count = {}

    for char in s:
        if char.isalnum():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    return odd_count <= 1

# 使用例
s1 = "Tact Coa"
s2 = "hello"
print(is_palindrome_permutation(s1))  # True
print(is_palindrome_permutation(s2))  # False
