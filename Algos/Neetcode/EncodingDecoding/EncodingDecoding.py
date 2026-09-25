# Encoding
# If the input list is empty, return an empty string.
#
# Create an empty list to store the sizes of each string.
#
# For each string, append its length to the sizes list.
# 
# Build a single string by:
#   Writing all sizes separated by commas.
#   Adding a '#' to mark the end of the size section.
#   Appending all the actual strings in order.
#   Return the final encoded string.
    
#   Decoding
#    If the encoded string is empty, return an empty list.
#    Read characters from the start until reaching '#' to extract all recorded sizes:
#    Parse each size by reading until a comma.
#    After the '#', extract substrings according to the sizes list:
#    For each size, read that many characters and append the substring to the result.
#    Return the list of decoded strings.


# 1. Take sentence and concat into one final string using length of string and # delimiter

def encode(sentence: list[str]) -> str:
    encoded_string = ""
    for word in sentence:
        encoded_string += str(len(word)) + "#" + word
    return encoded_string

def decode(s: str) -> list[str]:

    decoded_string = []
    i = 0
    while i < len(s):
        sizeStr = ""
        while s[i] != '#':
            sizeStr += s[i]
            i += 1
        size = int(sizeStr)
        i += 1
        decoded_string.append(s[i:i + size])
        i +=  size
    return decoded_string


# example 1
strs = ["hello", "world", "where", "are", "my", "burgers", "tonight"]
encoded_string = encode(strs)
print("encoded_string =", encoded_string)
decoded_strs = decode(encoded_string)
print("decoded_string =", decoded_strs)
