import struct


class DataBuffer:
    def __init__(self, data=None):
        self.rwpos = 0
        if(data == None):
            self.__writeBuff = bytearray()
            self.__read = False
        else:
            self.__readBuff = bytearray(data)
            self.__read = True

    def Size(self):
        if(self.__read):
            return len(self.__readBuff)
        else:
            return self.rwpos

    def ToArray(self):
        if(self.__read):
            return self.__readBuff
        else:
            return self.__writeBuff

    def SkipBytes(self, count):
        self.rwpos += count

    def WriteObject(self, obj):
        if type(obj) is int:
            self.__writeBuff.extend(struct.pack("<i", obj))
            return
        if type(obj) is str:
            self.WriteObject(len(obj))
            self.__writeBuff.extend(bytes(obj))
            return
        if type(obj) is float:
            self.__writeBuff.extend(struct.pack("<f", obj))
            return
        if type(obj) is bool:
            self.__writeBuff.append(obj)
            return

    def ReadInteger(self, Peek=True):
        if(not self.__read):
            raise Exception("Can't read from a write buffer")
        tmp = bytearray()
        tmp.append(self.__readBuff[self.rwpos])
        tmp.append(self.__readBuff[self.rwpos+1])
        tmp.append(self.__readBuff[self.rwpos+2])
        tmp.append(self.__readBuff[self.rwpos+3])
        if(Peek):
            self.rwpos += 4
        struc = struct.unpack("<i", tmp)
        return struc[0]

    def ReadString(self):
        if(not self.__read):
            raise Exception("Can't read from a write buffer")
        length = self.ReadInteger()
        tmp = bytearray()
        for i in range(length):
            tmp.append(self.__readBuff[self.rwpos+i])
        self.rwpos += length
        return tmp

    def ReadFloat(self, Peek=True):
        if(not self.__read):
            raise Exception("Can't read from a write buffer")
        tmp = bytearray()
        tmp.append(self.__readBuff[self.rwpos])
        tmp.append(self.__readBuff[self.rwpos+1])
        tmp.append(self.__readBuff[self.rwpos+2])
        tmp.append(self.__readBuff[self.rwpos+3])
        if(Peek):
            self.rwpos += 4
        struc = struct.unpack("<f", tmp)
        return struc[0]

    def ReadBoolean(self, Peek=True):
        if(not self.__read):
            raise Exception("Can't read from a write buffer")
        tmp = self.__readBuff[self.rwpos]
        if(Peek):
            self.rwpos += 1
        return bool(tmp)
