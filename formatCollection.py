from floatModel import FloatModel

fp64 = FloatModel(11, 52)
fp32 = FloatModel(8, 23)
fp16 = FloatModel(5, 10)

def freeFloat(
    exponentSize: int,
    mantissaSize: int,
    exponentBase: float = 2,
    exponentCarry: float = 2,
    mantissaCarry: float = 2,
    ):
        return FloatModel(exponentSize, mantissaSize, exponentBase, exponentCarry, mantissaCarry)