#definition of variables
sname = input('what is your name?\n')
iage = int(input('what is your age?\n'))
#
# get current year
import datetime
iyear = datetime.datetime.today().year
#
#calculate year person will reach 100 y.o.
ihundred = ((iyear-iage)+100)
sprint = print('Hello',sname,'. You will turn 100 in year',ihundred)
#
#Printing the previous message x amount of times
#where x is a number chosen by user
smult = input('please choose a number between 5 and 10')
imult = int(smult)
print(imult * sprint)
