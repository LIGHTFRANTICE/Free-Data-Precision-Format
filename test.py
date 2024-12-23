from baseModels import DataModel
import formatCollection as fc

dataBinStr = '0011010'

fm = fc.freeFloat(3, 3)

data = DataModel(dataBinStr, fm)

print(data.getValue())