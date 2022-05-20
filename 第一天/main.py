import os
from typing import List, Union

ET = "\n"


def get_data(filepath, length):
    if length <= 0:
        return [], []
    with open(filepath, "rb") as f:
        head = list(f.read(length))
        f.seek(-64, 2)
        tile = list(f.read(length))
        return head, tile


def print_hex(data: List[Union[int, None]], line_len: int = 16, /):
    for index, byte_int in enumerate(data):
        # 行号
        if index % line_len == 0:
            print(f"{ET if index else ''}{index // line_len:0>8b}", end="")
        elif index and (index % line_len) % 8 == 0:
            print("  |", end="")
        print("     " if byte_int is None else f"   {byte_int:0>2X}", end="")
    print()


if __name__ == '__main__':
    filepath = "../data/11652106806_.pic.jpg"
    length = 64
    show_length = 16
    # 二进制格式读取
    head, tile = get_data(filepath, length)
    getsize = os.path.getsize(filepath)
    print_hex(head + tile, show_length)
    print(f"结尾字节偏移{getsize % show_length}")
    print_hex(head + [None] * (getsize % show_length) + tile, show_length)
