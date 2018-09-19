#Definition of variables
shours = input('Enter the number of hours worked:\n')
srate = input('Value per hour:\n')
fhours = float(shours)
frate = float(srate)
#
#standard calculation
if fhours < 41:
    fstd = (fhours*frate)
    print(fstd)
#overtime calculation
else:
    fovt = ((fhours-40)*(frate*0.5))
    fstd = (fhours*frate)
    print(fstd+fovt)