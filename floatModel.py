from dataclasses import dataclass

@dataclass
class FloatModel:

    exponent: int
    mantissa: int
    exponentBase: float = 2
    exponentCarry: float = 2
    mantissaCarry: float = 2

    sign = 1

    def getExp(self, expBinStr: str, base: float, carry: float) -> float :

        expLen = len(expBinStr)

        bias = 0
        for i in range(expLen-1):
            bias += carry ** i

        e = 0
        for i in range(len(expBinStr)):
            e += int(expBinStr[-(i+1)]) * carry ** i

        return base ** (e - bias)

    def getMantissa(self, mantissaBinStr: str, carry: float) -> float :
        man = 0
        
        for bit in mantissaBinStr:
            man += int(bit) * carry ** -(mantissaBinStr.index(bit)+1)

        return man

    def getValue(self, dataBinStr: str) -> float:

        sign = 1 if dataBinStr[0]=="0" else -1

        exp = self.getExp(dataBinStr[1:(1+self.exponent)], base=2, carry=2)

        mantissa = self.getMantissa(dataBinStr[-self.mantissa:], carry=2)

        return sign * exp * mantissa

def singleModuleTest():

    fp64 = FloatModel(11, 52)
    fp32 = FloatModel(8, 23)
    fp16 = FloatModel(5, 10)

    dataBinStr = '00111111100100000000000000000000'

    v = fp32.getValue(dataBinStr)

    print(v==0.125)

if __name__ == "__main__":
    singleModuleTest()