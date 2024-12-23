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