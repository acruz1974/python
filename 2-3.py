#Define variables for hours and rate
nhours = input('Enter the number of hours worked:\n')
inhours = float(nhours)
hrate = input('Value per hour:\n')
ihrate = float(hrate)
tpay = inhours * ihrate
print('the total pay is',tpay,'euros')
