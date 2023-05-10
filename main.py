
class MyBigInt:
    # для нашого класу було обрано базу 2^32 щоб не було переповнень 64 бітів при перемножені
    __base = 4294967296

    def __init__(self):
        self.__number = [0]

    def getBin(self):
        first = True
        bin_num = ""
        for _num in self.__number:
            _num = bin(_num)[2:]
            if not first:
                if len(_num) < 32:
                    _num = "0"*(32-len(_num)) + _num
            bin_num += _num
            first = False
        return bin_num

    def setBin(self, bin_num: str):
        self.__number = []
        if "1" not in bin_num:
            self.__number = [0]
        else:
            first = True
            if len(bin_num) % 32 != 0:
                bin_num = "0" * (32 - len(bin_num) % 32) + bin_num
            while bin_num != "":
                _num = int(bin_num[:32], 2)
                if len(bin_num) > 32:
                    bin_num = bin_num[32:]
                else:
                    bin_num = ""
                if first and (_num == 0):
                    continue
                self.__number.append(_num)
                first = False

    def setHex(self, hex__number: str):
        self.__number = []
        hex__number.lower()
        hex_to_dec = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "a": 10,
            "b": 11,
            "c": 12,
            "d": 13,
            "e": 14,
            "f": 15
        }
        while len(hex__number) > 8:
            i = 0
            _num = 0
            for char in hex__number[:-9:-1]:
                _num += hex_to_dec[char] * pow(16, i)
                i += 1
            self.__number = [_num] + self.__number
            hex__number = hex__number[:-8]
        i = 0
        _num = 0
        for char in hex__number[::-1]:
            _num += hex_to_dec[char] * pow(16, i)
            i += 1
        self.__number = [_num] + self.__number

    def getHex(self):
        dec_to_hex = {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "a",
            11: "b",
            12: "c",
            13: "d",
            14: "e",
            15: "f"
        }
        hex_num = ""
        for _num in self.__number:
            hex_block = ""
            while _num != 0:
                hex_block = dec_to_hex[_num % 16] + hex_block
                _num = _num // 16
            if len(hex_block) < 8:
                hex_block = "0" * (8 - len(hex_block)) + hex_block
            hex_num += hex_block
        first = True
        buf = hex_num
        hex_num = ""
        for i in buf:
            if first and i == "0":
                continue
            first = False
            hex_num += i
        return hex_num

    def get_num(self):
        return self.__number

    def set_num(self, _num: list):
        self.__number = _num

    def INV(self):
        new__number = []
        first = True
        for _num in self.__number:
            _num = bin(_num)[2:]
            if not first:
                if len(_num) < 32:
                    _num = "0"*(32-len(_num)) + _num
            new_num = ""
            for bit in _num:
                if bit == "0":
                    new_num += "1"
                else:
                    new_num += "0"
            new_num = int(new_num, 2)
            new__number.append(new_num)
            first = False
        self.__number = new__number

    @staticmethod
    def XOR(_num1, _num2):
        bin_num1 = _num1.getBin()
        bin_num2 = _num2.getBin()
        if len(bin_num1) > len(bin_num2):
            bin_num2 = "0"*(len(bin_num1)-len(bin_num2)) + bin_num2
        elif len(bin_num2) > len(bin_num1):
            bin_num1 = "0"*(len(bin_num2)-len(bin_num1)) + bin_num1
        bin_num_res = ""
        for bit1, bit2 in zip(bin_num1, bin_num2):
            if (bit1 == "0" and bit2 == "0") or (bit2 == "1" and bit1 == "1"):
                bin_num_res += "0"
            else:
                bin_num_res += "1"
        _num_res = MyBigInt()
        _num_res.setBin(bin_num_res)
        return _num_res

    @staticmethod
    def AND(_num1, _num2):
        bin_num1 = _num1.getBin()
        bin_num2 = _num2.getBin()
        if len(bin_num1) > len(bin_num2):
            bin_num2 = "0"*(len(bin_num1)-len(bin_num2)) + bin_num2
        elif len(bin_num2) > len(bin_num1):
            bin_num1 = "0"*(len(bin_num2)-len(bin_num1)) + bin_num1
        bin_num_res = ""
        for bit1, bit2 in zip(bin_num1, bin_num2):
            if bit1 == "1" and bit2 == "1":
                bin_num_res += "1"
            else:
                bin_num_res += "0"
        _num_res = MyBigInt()
        _num_res.setBin(bin_num_res)
        return _num_res

    @staticmethod
    def OR(_num1, _num2):
        bin_num1 = _num1.getBin()
        bin_num2 = _num2.getBin()
        if len(bin_num1) > len(bin_num2):
            bin_num2 = "0" * (len(bin_num1) - len(bin_num2)) + bin_num2
        elif len(bin_num2) > len(bin_num1):
            bin_num1 = "0" * (len(bin_num2) - len(bin_num1)) + bin_num1
        bin_num_res = ""
        for bit1, bit2 in zip(bin_num1, bin_num2):
            if bit1 == "0" and bit2 == "0":
                bin_num_res += "0"
            else:
                bin_num_res += "1"
        _num_res = MyBigInt()
        _num_res.setBin(bin_num_res)
        return _num_res

    def shiftR(self, n):
        bin_num = self.getBin()
        if n >= len(bin_num):
            self.__number = [0]
        else:
            bin_num = bin_num[:-n]
            self.setBin(bin_num)

    def shiftL(self, n):
        bin_num = self.getBin()
        bin_num += "0" * n
        self.setBin(bin_num)

    @staticmethod
    def ADD(_num1, _num2):
        _num1 = _num1.get_num()[:]
        _num2 = _num2.get_num()[:]
        if len(_num1) > len(_num2):
            _num2 = [0] * (len(_num1) - len(_num2)) + _num2
        elif len(_num2) > len(_num1):
            _num1 = [0] * (len(_num2) - len(_num1)) + _num1
        buf = 0
        for i in range(len(_num1)-1,-1,-1):
            _num = _num1[i] + _num2[i] + buf
            if _num >= MyBigInt.__base:
                _num = _num % MyBigInt.__base
                buf = 1
            else:
                buf = 0
            _num1[i] = _num
        if buf == 1:
            _num1 = [1] + _num1
        _num2 = MyBigInt()
        _num2.set_num(_num1)
        return _num2

    @staticmethod
    def SUB(_num1, _num2):
        _num1 = _num1.get_num()[:]
        _num2 = _num2.get_num()[:]
        if len(_num1) > len(_num2):
            _num2 = [0] * (len(_num1) - len(_num2)) + _num2
        buf = 0
        for i in range(len(_num1) - 1, -1, -1):
            _num1[i] = _num1[i] + buf
            if _num1[i] < _num2[i]:
                _num1[i] = _num1[i] + MyBigInt.__base - _num2[i]
                buf = -1
            else:
                _num1[i] -= _num2[i]
                buf = 0
        _num2 = MyBigInt()
        _num2.set_num(_num1)
        return _num2

    def is_bigger(self, _num):
        _num = _num.get_num()[:]
        if len(self.__number) > len(_num):
            return True
        if len(self.__number) < len(_num):
            return False
        for a, b in zip(self.__number, _num):
            if a < b:
                return False
            if a > b:
                return True
        return False

    def equal(self, _num):
        _num = _num.get_num()[:]
        if len(self.__number) > len(_num):
            return False
        if len(self.__number) < len(_num):
            return False
        for a, b in zip(self.__number, _num):
            if a < b:
                return False
            if a > b:
                return False
        return True

    def is_lower(self, _num):
        _num = _num.get_num()[:]
        if len(self.__number) > len(_num):
            return False
        if len(self.__number) < len(_num):
            return True
        for a, b in zip(self.__number, _num):
            if a < b:
                return True
            if a > b:
                return False
        return False

    # @staticmethod
    # def MUL(_num1, _num2):
    #     if len(_num1.get_num()) < len(_num2.get_num()):
    #         _num1, _num2 = _num2, _num1
    #     if len(_num2.get_num()) == 1:
    #         _num1 = _num1.get_num()
    #         _num2 = _num2.get_num()[0]
    #         buf = 0
    #         for i in range(len(_num1)-1,-1,-1):
    #             _num = _num1[i] * _num2
    #             _num1[i] = _num % MyBigInt.__base + buf
    #             buf = _num // MyBigInt.__base
    #         _num2 = MyBigInt()
    #         _num2.set_num(_num1)
    #         return _num2
    #     m = len(_num1.get_num()) // 2
    #     a1, b1 = _num1.get_num()[:m], _num1.get_num()[m:]
    #     if len(_num2.get_num()) <= m:
    #         a2, b2 = [0], _num2.get_num()
    #     else:
    #         a2, b2 = _num2.get_num()[:(len(_num2.get_num())-m)], _num2.get_num()[(len(_num2.get_num())-m):]
    #     _num_a1 = MyBigInt()
    #     _num_a2 = MyBigInt()
    #     _num_b1 = MyBigInt()
    #     _num_b2 = MyBigInt()
    #     _num_a1.set_num(a1)
    #     _num_a2.set_num(a2)
    #     _num_b1.set_num(b1)
    #     _num_b2.set_num(b2)
    #     z0 = MyBigInt.MUL(_num_b1, _num_b2)
    #     z1 = MyBigInt.MUL(MyBigInt.ADD(_num_a1, _num_b1), MyBigInt.ADD(_num_a2, _num_b2))
    #     z2 = MyBigInt.MUL(_num_a1, _num_a2)
    #     a = [1] + [0] * m * 2
    #     _num = MyBigInt()
    #     _num.set_num(a)
    #     a = _num
    #     b = [1] + [0] * m
    #     _num = MyBigInt()
    #     _num.set_num(b)
    #     b = _num
    #     return MyBigInt.ADD(MyBigInt.ADD(MyBigInt.MUL(z2, a), MyBigInt.MUL(MyBigInt.SUB(MyBigInt.SUB(z1, z2), z0), b)), z0)

    @staticmethod
    def MOD(_num1, _num2):
        if _num1.equal(_num2):
            return MyBigInt().set_num([0])
        while _num1.is_bigger(_num2) or _num1.equal(_num2):
            _num1 = MyBigInt.SUB(_num1, _num2)
        return _num1




if __name__ == '__main__':
    num11 = MyBigInt()
    num21 = MyBigInt()
    num31 = MyBigInt()
    num11.setHex("51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4")
    num21.setHex("403db8ad88a3932a0b7e8189aed9eeffb8121dfac05c3512fdb396dd73f6331c")
    print("getHex")
    print(num11.getHex())
    print(num21.getHex())
    num31 = MyBigInt.XOR(num11, num21)
    print("XOR")
    print(num31.getHex())
    num31 = MyBigInt.OR(num11, num21)
    print("OR")
    print(num31.getHex())
    num31.INV()
    print("INV")
    print(num31.getHex())
    num31 = MyBigInt.AND(num11, num21)
    print("AND")
    print(num31.getHex())
    num31.shiftR(3)
    print("shiftR")
    print(num31.getHex())
    num31.shiftL(5)
    print("shiftL")
    print(num31.getHex())
    num11.setHex("36f028580bb02cc8272a9a020f4200e346e276ae664e45ee80745574e2f5ab80")
    num21.setHex("70983d692f648185febe6d6fa607630ae68649f7e6fc45b94680096c06e4fadb")
    num31 = MyBigInt.ADD(num11, num21)
    print("ADD")
    print(num31.getHex())
    num11.setHex("33ced2c76b26cae94e162c4c0d2c0ff7c13094b0185a3c122e732d5ba77efebc")
    num21.setHex("22e962951cb6cd2ce279ab0e2095825c141d48ef3ca9dabf253e38760b57fe03")
    num31 = MyBigInt.SUB(num11, num21)
    print("SUB")
    print(num31.getHex())
    num21.setHex("1")
    num21 = MyBigInt.ADD(num11, num21)
    num21 = MyBigInt.ADD(num11, num21)
    print("MOD")
    num31 = MyBigInt.MOD(num21, num11)
    print(num21.getHex())
    print(num31.getHex())




