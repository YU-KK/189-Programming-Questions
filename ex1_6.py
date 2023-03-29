def compress_string(s: str) -> str:
    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1

    compressed.append(s[-1] + str(count))
    compressed_string = ''.join(compressed)

    if len(compressed_string) < len(s):
        return compressed_string
    else:
        return s


input_string = "aabcccccaaa"
compressed_string = compress_string(input_string)
print(compressed_string)  # Output: "a2b1c5a3"
