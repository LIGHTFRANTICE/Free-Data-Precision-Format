from dataclasses import dataclass
from floatModel import FloatModel

@dataclass
class DataModel:
    data: str
    format: FloatModel | None
    def getValue(self,) -> float:
        if self.format is None:
            raise TypeError("No data precision format provided!")
        else:
            return self.format.getValue(self.data)

@dataclass
class FormatCollection:

    fp64 = FloatModel(11, 52)
    fp32 = FloatModel(8, 23)
    fp16 = FloatModel(5, 10)

    def freeFloat(
            self, 
            exponentSize: int,
            mantissaSize: int,
            exponentBase: float = 2,
            exponentCarry: float = 2,
            mantissaCarry: float = 2,
        ):
            return FloatModel(exponentSize, mantissaSize, exponentBase, exponentCarry, mantissaCarry)