import mmap
import os

if __name__ == '__main__':


    with open("../data/急性腹膜炎.txt") as f:
        with mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ) as m:
            print("前十个字符",m.read(1))
            print("前十个字符",m[:10])
            print("前十个字符",m[:20])
            print("前十个字符",m.read(10))

