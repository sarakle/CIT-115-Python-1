sName = input('What is your name: ')
nWeight = float(input('What is your weight: '))

nMERCURY_WEIGHT = 0.38
nVENUS_WEIGHT = 0.91
nMOON_WEIGHT = 0.165
nMARS_WEIGHT = 0.38
nJUPITER_WEIGHT = 2.34
nSATURN_WEIGHT = 0.93
nURANUS_WEIGHT = 0.92
nNEPTUNE_WEIGHT = 1.12
nPLUTO_WEIGHT = 0.066

nWEIGHT_CONVERSION1 = nWeight * nMERCURY_WEIGHT
nWEIGHT_CONVERSION2 = nWeight * nVENUS_WEIGHT
nWEIGHT_CONVERSION3 = nWeight * nMOON_WEIGHT
nWEIGHT_CONVERSION4 = nWeight * nMARS_WEIGHT
nWEIGHT_CONVERSION5 = nWeight * nJUPITER_WEIGHT
nWEIGHT_CONVERSION6 = nWeight * nSATURN_WEIGHT
nWEIGHT_CONVERSION7 = nWeight * nURANUS_WEIGHT
nWEIGHT_CONVERSION8 = nWeight * nNEPTUNE_WEIGHT
nWEIGHT_CONVERSION9 = nWeight * nPLUTO_WEIGHT

print(format(sName),"here are your weights on our Solar System's planets: ")
print( '{:20}'.format("Weight of Mercury: ") + format(nWEIGHT_CONVERSION1, "20,.2f"))
print( '{:20}'.format("Weight of Venus: ") + format(nWEIGHT_CONVERSION2, "20,.2f"))
print( '{:20}'.format("Weight of Moon: ") + format(nWEIGHT_CONVERSION3, "20,.2f"))
print( '{:20}'.format("Weight of Mars: ") + format(nWEIGHT_CONVERSION4, "20,.2f"))
print( '{:20}'.format("Weight of Jupiter: ") + format(nWEIGHT_CONVERSION5, "20,.2f"))
print( '{:20}'.format("Weight of Saturn: ") + format(nWEIGHT_CONVERSION6, "20,.2f"))
print( '{:20}'.format("Weight of Uranus: ") + format(nWEIGHT_CONVERSION7, "20,.2f"))
print( '{:20}'.format("Weight of Neptune: ") + format(nWEIGHT_CONVERSION8, "20,.2f"))
print( '{:20}'.format("Weight of Pluto: ") + format(nWEIGHT_CONVERSION9, "20,.2f"))

