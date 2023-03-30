from pacing import *

"""
Example script that can be used to calculate your racing pace. First a global racing
pace is determined and afterwards a more detailed race plan can be evaluated.
"""
print("Global racing pace")
calcPacing(21.0975, hours = 1, minutes = 50)

print("\nDetailed racing pace per 3 section")
total  = calcRevPacing(dist = 7.0325, minutes = 5, seconds = 20,  printresult = True)
total += calcRevPacing(dist = 7.0325, minutes = 5, seconds = 13,  printresult = True)
total += calcRevPacing(dist = 7.0325, minutes = 5, seconds =  6,  printresult = True)
print("Check if this is the same as your total running time: " + str(total))

print("\nPrinting sequence of pacings to be able to investigate pacing")
for i in range(0,10):
	calcPacing(21.0975, hours = 1, minutes = 50+i)