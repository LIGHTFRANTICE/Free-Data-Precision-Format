from baseModels import DataModel, FormatCollection

dataBinStr = '0011010'

fm = FormatCollection().freeFloat(3, 3)

data = DataModel(dataBinStr, fm)

print(data.getValue())