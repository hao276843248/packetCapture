import mmap
import os
import struct
import time


def readPackData(f):
    f.read(10)


class PackData():
    # 端序 -1：大 1:小
    endianness = 1
    LinkType = 1
    Caplen = 1
    thisZone = 1
    SigFigs = 1
    data = None
    fileSize = 0
    PacketData = 0

    nextPacketlist = []

    def __init__(self, filePath):
        self.fileSize = os.path.getsize(filePath)  # 获得文件大小
        with open(filePath) as f:
            self.data = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        if self.data[:4].hex() == "d4c3b2a1":
            self.endianness = -1

    def raed(self):
        t = time.localtime(int(m[24:28][::-1].hex(), 16))
        print(time.strftime("%Y-%m-%d %H:%M:%S", t))
        self.data

    def randNextPacket(self, start, index):
        self.data[start:self.nextPacketlist[index]]

    def readPacket(self, pData):
        tT = time.localtime(int(pData[:4][::self.endianness].hex(), 16))
        tL = time.localtime(int(pData[4:8][::self.endianness].hex(), 16))
        timestampTop = time.strftime("%Y-%m-%d %H:%M:%S", t)
        timestampLow = time.strftime("%Y-%m-%d %H:%M:%S", t)
        Caplen = int(pData[8:12][::self.endianness].hex(), 16)
        Len = int(pData[12:16][::self.endianness].hex(), 16)
        data = pData[16:Caplen][::self.endianness].hex()
        self.nextPacketlist.append(Caplen)

    def close(self):
        self.data.close()


if __name__ == '__main__':
    with open("../data/day3.pcap") as f:
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
            t = time.localtime(int(m[24:28][::-1].hex(), 16))
            print(time.strftime("%Y-%m-%d %H:%M:%S", t))

            print(int(m[36:40][::-1].hex(), 16))
