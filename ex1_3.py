def urlify(s: str, true_length: int) -> str:
    s = s[:true_length]  # 追加用スペースを除く
    return s.replace(" ", "%20")  # 空白文字を"%20"で置き換える

# 使用例
input_string = "Mr John Smith"
true_length = 13

result = urlify(input_string, true_length)
print(result)  # "Mr%20John%20Smith" を出力
