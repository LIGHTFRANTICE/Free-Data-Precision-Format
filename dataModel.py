from dataclasses import dataclass
from floatModel import FloatModel

@dataclass
class DataModel:
    data: str
    format: FloatModel | None

    def getValue(self) -> float:
        if self.format is None:
            raise TypeError("No data precision format provided!")
        else:
            return self.format.getValue(self.data)
    
    def __add__(self, other):
        if self.format != other.format:
            raise TypeError("invalid call of add, please use the same format.")
        
        if self.format is None:
            raise TypeError("Data is not formatted.")
        else:
            return DataModel(self.format.__add__(self.data, other.data), self.format)