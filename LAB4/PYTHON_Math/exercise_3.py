import math
sidel = 25
siden = 4
apoth = sidel / (2 *math.tan(math.pi/siden))
answer = (sidel * siden) * apoth / 2
print(round(answer, 1))