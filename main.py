
class MyBigInt:
    # для нашого класу було обрано базу 2^32 щоб не було переповнень 64 бітів при перемножені
    __base = 4294967296

    def __init__(self):
        self.__number = [0]

    def getBin(self):
        first = True
        bin_num = ""
        for num in self.__number:
            num = bin(num)[2:]
            if not first:
                if len(num) < 32:
                    num = "0"*(32-len(num)) + num
            bin_num += num
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
                num = int(bin_num[:32], 2)
                if len(bin_num) > 32:
                    bin_num = bin_num[32:]
                else:
                    bin_num = ""
                if first and (num == 0):
                    continue
                self.__number.append(num)
                first = False

    def setHex(self, hex_number: str):
        self.__number = []
        hex_number.lower()
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
        while len(hex_number) > 8:
            i = 0
            num = 0
            for char in hex_number[:-9:-1]:
                num += hex_to_dec[char] * pow(16, i)
                i += 1
            self.__number = [num] + self.__number
            hex_number = hex_number[:-8]
        i = 0
        num = 0
        for char in hex_number[::-1]:
            num += hex_to_dec[char] * pow(16, i)
            i += 1
        self.__number = [num] + self.__number

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
        for num in self.__number:
            hex_block = ""
            while num != 0:
                hex_block = dec_to_hex[num % 16] + hex_block
                num = num // 16
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

    def set_num(self, num: list):
        self.__number = num

    def INV(self):
        new_number = []
        first = True
        for num in self.__number:
            num = bin(num)[2:]
            if not first:
                if len(num) < 32:
                    num = "0"*(32-len(num)) + num
            new_num = ""
            for bit in num:
                if bit == "0":
                    new_num += "1"
                else:
                    new_num += "0"
            new_num = int(new_num, 2)
            new_number.append(new_num)
            first = False
        self.__number = new_number

    @staticmethod
    def XOR(num1, num2):
        bin_num1 = num1.getBin()
        bin_num2 = num2.getBin()
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
        num_res = MyBigInt()
        num_res.setBin(bin_num_res)
        return num_res

    @staticmethod
    def AND(num1, num2):
        bin_num1 = num1.getBin()
        bin_num2 = num2.getBin()
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
        num_res = MyBigInt()
        num_res.setBin(bin_num_res)
        return num_res

    @staticmethod
    def OR(num1, num2):
        bin_num1 = num1.getBin()
        bin_num2 = num2.getBin()
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
        num_res = MyBigInt()
        num_res.setBin(bin_num_res)
        return num_res

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
    def ADD(num1, num2):
        num1 = num1.get_num()
        num2 = num2.get_num()
        if len(num1) > len(num2):
            num2 = [0] * (len(num1) - len(num2)) + num2
        elif len(num2) > len(num1):
            num1 = [0] * (len(num2) - len(num1)) + num1
        buf = 0
        for i in range(len(num1)-1,-1,-1):
            num = num1[i] + num2[i] + buf
            if num >= MyBigInt.__base:
                num = num % MyBigInt.__base
                buf = 1
            else:
                buf = 0
            num1[i] = num
        if buf == 1:
            num1 = [1] + num1
        num2 = MyBigInt()
        num2.set_num(num1)
        return num2

    @staticmethod
    def SUB(num1, num2):
        num1 = num1.get_num()
        num2 = num2.get_num()
        if len(num1) > len(num2):
            num2 = [0] * (len(num1) - len(num2)) + num2
        buf = 0
        for i in range(len(num1) - 1, -1, -1):
            num1[i] = num1[i] + buf
            if num1[i] < num2[i]:
                num1[i] = num1[i] + MyBigInt.__base - num2[i]
                buf = -1
            else:
                num1[i] -= num2[i]
                buf = 0
        num2 = MyBigInt()
        num2.set_num(num1)
        return num2

    def is_bigger(self, num):
        num = num.get_num()
        if len(self.__number) > len(num):
            return True
        if len(self.__number) < len(num):
            return False
        for a, b in zip(self.__number, num):
            if a < b:
                return False
            if a > b:
                return True
        return False

    def equal(self, num):
        num = num.get_num()
        if len(self.__number) > len(num):
            return False
        if len(self.__number) < len(num):
            return False
        for a, b in zip(self.__number, num):
            if a < b:
                return False
            if a > b:
                return False
        return True

    def is_lower(self, num):
        num = num.get_num()
        if len(self.__number) > len(num):
            return False
        if len(self.__number) < len(num):
            return True
        for a, b in zip(self.__number, num):
            if a < b:
                return True
            if a > b:
                return False
        return False

    # @staticmethod
    # def MUL(num1, num2):
    #     if len(num1.get_num()) < len(num2.get_num()):
    #         num1, num2 = num2, num1
    #     if len(num2.get_num()) == 1:
    #         num1 = num1.get_num()
    #         num2 = num2.get_num()[0]
    #         buf = 0
    #         for i in range(len(num1)-1,-1,-1):
    #             num = num1[i] * num2
    #             num1[i] = num % MyBigInt.__base + buf
    #             buf = num // MyBigInt.__base
    #         num2 = MyBigInt()
    #         num2.set_num(num1)
    #         return num2
    #     m = len(num1.get_num()) // 2
    #     a1, b1 = num1.get_num()[:m], num1.get_num()[m:]
    #     if len(num2.get_num()) <= m:
    #         a2, b2 = [0], num2.get_num()
    #     else:
    #         a2, b2 = num2.get_num()[:(len(num2.get_num())-m)], num2.get_num()[(len(num2.get_num())-m):]
    #     num_a1 = MyBigInt()
    #     num_a2 = MyBigInt()
    #     num_b1 = MyBigInt()
    #     num_b2 = MyBigInt()
    #     num_a1.set_num(a1)
    #     num_a2.set_num(a2)
    #     num_b1.set_num(b1)
    #     num_b2.set_num(b2)
    #     z0 = MyBigInt.MUL(num_b1, num_b2)
    #     z1 = MyBigInt.MUL(MyBigInt.ADD(num_a1, num_b1), MyBigInt.ADD(num_a2, num_b2))
    #     z2 = MyBigInt.MUL(num_a1, num_a2)
    #     a = [1] + [0] * m * 2
    #     num = MyBigInt()
    #     num.set_num(a)
    #     a = num
    #     b = [1] + [0] * m
    #     num = MyBigInt()
    #     num.set_num(b)
    #     b = num
    #     return MyBigInt.ADD(MyBigInt.ADD(MyBigInt.MUL(z2, a), MyBigInt.MUL(MyBigInt.SUB(MyBigInt.SUB(z1, z2), z0), b)), z0)

    @staticmethod
    def MOD(num1, num2):
        if num1.equal(num2):
            return MyBigInt().set_num([0])
        while num1.is_bigger(num2) or num1.equal(num2):
            num1 = MyBigInt.SUB(num1, num2)
        return num1




if __name__ == '__main__':
    num1 = MyBigInt()
    num2 = MyBigInt()
    num3 = MyBigInt()
    num1.setHex("51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4")
    num2.setHex("403db8ad88a3932a0b7e8189aed9eeffb8121dfac05c3512fdb396dd73f6331c")
    print("getHex")
    print(num1.getHex())
    print(num2.getHex())
    num3 = MyBigInt.XOR(num1, num2)
    print("XOR")
    print(num3.getHex())
    num3 = MyBigInt.OR(num1, num2)
    print("OR")
    print(num3.getHex())
    num3.INV()
    print("INV")
    print(num3.getHex())
    num3 = MyBigInt.AND(num1, num2)
    print("AND")
    print(num3.getHex())
    num3.shiftR(3)
    print("shiftR")
    print(num3.getHex())
    num3.shiftL(5)
    print("shiftL")
    print(num3.getHex())
    num1.setHex("36f028580bb02cc8272a9a020f4200e346e276ae664e45ee80745574e2f5ab80")
    num2.setHex("70983d692f648185febe6d6fa607630ae68649f7e6fc45b94680096c06e4fadb")
    num3 = MyBigInt.ADD(num1, num2)
    print("ADD")
    print(num3.getHex())
    num1.setHex("33ced2c76b26cae94e162c4c0d2c0ff7c13094b0185a3c122e732d5ba77efebc")
    num2.setHex("22e962951cb6cd2ce279ab0e2095825c141d48ef3ca9dabf253e38760b57fe03")
    num3 = MyBigInt.SUB(num1, num2)
    print("SUB")
    print(num3.getHex())
    num3 = MyBigInt.MOD(num1, num2)
    print("MOD")
    print(num3.getHex())




