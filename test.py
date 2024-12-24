from dataModel import DataModel
import formatCollection as fc

dataBinStr0 = '0011010'
dataBinStr1 = '0011010'

fm = fc.freeFloat(3, 3)

data0 = DataModel(dataBinStr0, fm)
data1 = DataModel(dataBinStr1, fm)

print(data0.getValue())
print(data1.getValue())

print((data0+data1).getValue())