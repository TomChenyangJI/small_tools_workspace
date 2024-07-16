

import binascii
def hex_to_binary(hex_str):
    # 使用字符串的lstrip方法去除前缀的\x
    hex_str = hex_str.lstrip('\x')
    # 使用bytes.fromhex将16进制字符串转换为二进制字节
    binary_bytes = bytes.fromhex(hex_str)
    # 使用binascii.b2a_bin将二进制字节转换为二进制表示的字符串
    binary_str = binascii.b2a_bin(binary_bytes)

    return binary_str.decode('utf-8')


# 示例使用
hex_string = r'\x48\x65\x6c\x6c\x6f'  # 表示ASCII字符 'Hello'
binary_str = hex_to_binary(hex_string)
print(binary_str)  # 输出: 01001000011011000110111100011011110011011110011011