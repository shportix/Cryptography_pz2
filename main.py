
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
        return hex_num

    def get_num(self):
        return self.__number

    def set_num(self, num: list):
        self.__number = num

    def inv(self):
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


if __name__ == '__main__':
    num1 = MyBigInt()
    num2 = MyBigInt()
    num2.setHex("22e962951cb6cd2ce279ab0e2095825c141d48ef3ca9dabf253e38760b57fe03")
    num1.setHex("33ced2c76b26cae94e162c4c0d2c0ff7c13094b0185a3c122e732d5ba77efebc")
    num3 = MyBigInt.SUB(num1, num2)
    print(num3.getHex())
    print("10e570324e6ffdbc6b9c813dec968d9bad134bc0dbb061530934f4e59c2700b9")
    num4 = MyBigInt()
    num4.setHex("10e570324e6ffdbc6b9c813dec968d9bad134bc0dbb061530934f4e59c2700b9")
    print(num3.get_num())
    print(num4.get_num())
    print(2 % 7)

# 3298604640442880686462402446080864228606228608240086282646406628
# 4746068600828626042008240048662648680004848888466408662286800880
# 8044673241271506728470642494743512908611077496706494944933207508



