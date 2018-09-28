#Definition of variables
shours = input('Enter the number of hours worked:\n')
srate = input('Value per hour:\n')
#Sanity check
try:
    fhours = float(shours)
    frate = float(srate)
except:
    print('insert numeric number')
    quit()
#
# Function to calculate overtime
def computepay():
    fovt = ((fhours-40)*(frate*0.5))
    fstd = (fhours*frate)
    ftotal = (fstd+fovt)
    return ftotal
#standard calculation
if fhours < 41:
    fstd = (fhours*frate)
    print(fstd)
#overtime calculation
else:
    ftotal = computepay()
    print(ftotal)