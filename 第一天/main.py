import os
import struct

if __name__ == '__main__':
    filepath = "../data/11652106806_.pic.jpg"
    # 二进制格式读取
    with open(filepath, "rb") as f:
        size = os.path.getsize(filepath)  # 获得文件大小
        hexs = ""
        ints = ""
        print()
        for i in range(16):
            data = f.read(1)
            # 10进制
            ints += " " + str(struct.unpack("B", data)[0])
            # hex 格式 16进制
            hexs += " " + data.hex()
        hexs += "\n"
        ints += "\n"
        # 读取文件的光标偏移到结尾的前16个字节
        f.seek(size - 16)
        for i in range(16):
            data = f.read(1)
            # 10进制
            ints += " " + str(struct.unpack("B", data)[0])
            # hex 格式 16进制
            hexs += " " + data.hex()
        print(hexs.upper())
        print()
        print(ints.upper())
