# Variable definition
snumber=input('Enter a number between 0.0 and 1.0')
# Sanity check
try:
    fnumber=float(snumber)
except:
    print('Enter a numeric number')
    quit()
#
# Grades
if fnumber < 0.0: 
    print('out of range value')
    quit()
elif fnumber > 1.0:
    print('out of range value')
    quit()
elif fnumber >= 0.9:
    print('A')
elif fnumber >= 0.8:
    print('B')
elif fnumber >= 0.7:
    print('C')
elif fnumber >= 0.6:
    print('D')
else:
    fnumber < 0.6
    print('F')
