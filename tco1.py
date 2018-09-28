# Basic cost savings Tool
#
# Constants - Please update prices here
# Electricity
f_electricity_cost_eu = 0               # avg KW/h Europe
f_electricity_cost_us = 0               # avg KW/h USA
f_electricity_cost_hk = 0               # avg KW/h Hong Kong
# Host Support
f_support_eu = 0                        # avg support cost Europe
f_support_us = 0                        # avg support cost USA
f_support_us = 0                        # avg support Hong Kong
# licence price based on region and product
i_DS10_EU = 7260
i_DS20_EU = 7260
i_ES40_EU = 11230
i_GS160_EU = 33290
i_GS320_EU = 60110
i_GS80_EU = 19170
i_400_EU = 2980
i_4100_EU = 11230
i_A408_EU = 4480
i_A410_EU = 8400
i_A510_EU = 19280
i_A520_EU = 29150
i_N4010_EU = 24220
i_N4020_EU = 34030
i_N4030_EU = 41460
i_N4040_EU = 48830
i_N4060_EU = 58700
i_N4080_EU = 68570
i_4ML10_EU = 2550
i_4ML20_EU = 4280
i_4UL20_EU = 5130
i_4UL30_EU = 7580
i_4UL40_EU = 14400
i_4UL50_EU = 23490
i_XKPlus_EU = 9760
i_XL_EU = 9760
i_XLPlus_EU = 16220
i_XM_EU = 3460
i_XMPlus_EU = 6520
i_6610Plus_EU = 25130
i_6620Plus_EU = 33660
i_6630Plus_EU = 38850
i_6660Plus_EU = 51790
i_2000_EU = 4820
i_DS10_US = 5540
i_DS20_US = 7110
i_ES40_US = 15450
i_GS160_US = 28570
i_GS320_US = 35560
i_GS80_US = 20410
i_400_US = 4020
i_4100_US = 9620
i_A408_US = 5250
i_A410_US = 9910
i_A510_US = 22740
i_A520_US = 34400
i_N4010_US = 28570
i_N4020_US = 40230
i_N4030_US = 48970
i_N4040_US = 57720
i_N4060_US = 69380
i_N4080_US = 81040
i_4ML10_US = 3360
i_4ML20_US = 5620
i_4UL20_US = 6740
i_4UL30_US = 9950
i_4UL40_US = 18920
i_4UL50_US = 30860
i_XKPlus_US = 17430
i_XL_US = 17430
i_XLPlus_US = 28570
i_XM_US = 6270
i_XMPlus_US = 11600
i_6610Plus_US = 28570
i_6620Plus_US = 37900
i_6630Plus_US = 43730
i_6660Plus_US = 58300
i_2000_US = 5540
i_DS10_HK = 5930
i_DS20_HK = 7930
i_ES40_HK = 18920
i_GS160_HK = 35020
i_GS320_HK = 82960
i_GS80_HK = 25010
i_400_HK = 5000
i_4100_HK = 18920
i_A408_HK = 6130
i_A410_HK = 11570
i_A510_HK = 26540
i_A520_HK = 40150
i_N4010_HK = 33350
i_N4020_HK = 46960
i_N4030_HK = 57170
i_N4040_HK = 67370
i_N4060_HK = 80980
i_N4080_HK = 94590
i_4ML10_HK = 4040
i_4ML20_HK = 6740
i_4UL20_HK = 8090
i_4UL30_HK = 11950
i_4UL40_HK = 22700
i_4UL50_HK = 37030
i_XKPlus_HK = 14900
i_XL_HK = 14900
i_XLPlus_HK = 24700
i_XM_HK = 5310
i_XMPlus_HK = 9910
i_6610Plus_HK = 28570
i_6620Plus_HK = 37900
i_6630Plus_HK = 43730
i_6660Plus_HK = 58300
i_2000_HK = 8100
#variables that will receive input
f_electricity_cost = 0                  # avg KW/h based on region
f_support = 0                           # avg support cost based on region
f_licence = 0                           # licence price
f_maintenance = 0
i_cpu = 0
i_location = 0
print('Cost Savings Tool\n')
print('\n')
print('Choose your system')
print('\n')
print('(1)Alpha')
print('(2)HP3000 / HP9000')
print('(3)Sun)')
print('(4)VAX')
ssystem = (input('your choice? '))
while (ssystem != '1') and (ssystem != '2') and (ssystem !='3') and (ssystem != '4'):
    input('choose a valid option ')
if ssystem == '1':
    print('(1)AlphaServer 400','    (7)AlphaServer 2100')
    print('(2)AlphaServer 1000','   (8)AlphaServer 4100')
    print('(3)AlphaServer 800','    (9)AlphaServer DS10')
    print('(4)AlphaServer 1200','   (10)AlphaServer DS20')
    print('(5)AlphaServer 2000','   (11)AlphaServer ES40')
    print('(6)AlphaServer 4000','   (12)AlphaServer GS80/160/320')
    imodel = input('your choice? ')
#    while imodel != range(1,12):
#        input('choose a valid option')
    if (imodel == '1') or (imodel == '2'):
        i_cpu = 1
        f_licence = i_400_EU
        f_maintenance = float(input('How much do you pay per year? '))
        print('Where are you located?')
        print('(1) Europe','    (2)Americas','     (3)Asia')
        i_location = int(input('Your choice?'))
    elif (imodel == '3'):
        i_cpu = 1
        f_licence = i_2000_EU
        f_maintenance = float(input('How much do you pay per year? '))
        print('Where are you located?')
        print('(1) Europe','    (2)Americas','     (3)Asia')
        i_location = int(input('Your choice?'))
    elif (imodel == '4') or (imodel == '5') or (imodel == '6'):
        print('CPU: ')
        print('(1)CPU',' (2)CPU')
        i_number_cpus = int(input('How many CPUs? '))
        i_cpu = i_number_cpus
        f_licence = i_2000_EU
        f_maintenance = float(input('How much do you pay per year? '))
        print('Where are you located?')
        print('(1) Europe','    (2)Americas','     (3)Asia')
        i_location = int(input('Your choice?'))
    elif (imodel == '7') or (imodel == '8'):
        print('CPs: ')
        print('(1)CPU',' (2)CPU', '   (3)CPU', '    (4)CPU')
        i_number_cpus = int(input('How many CPUs? '))
        i_cpu = i_number_cpus
        f_licence = i_4100_EU
        f_maintenance = float(input('How much do you pay per year? '))
        print('Where are you located?')
        print('(1) Europe','    (2)Americas','     (3)Asia')
        i_location = int(input('Your choice?'))
    elif (imodel == '9'):
        i_cpu = 1
        f_licence = i_DS10_EU
        f_maintenance = float(input('How much do you pay per year? '))
        print('Where are you located?')
        print('(1) Europe','    (2)Americas','     (3)Asia')
        i_location = int(input('Your choice?'))
    elif (imodel == '10'):
        print('CPU: ')
        print('(1)CPU',' (2)CPU')
        i_number_cpus = int(input('How many CPUs? '))
        i_cpu = i_number_cpus
        f_licence = i_DS20_EU
        f_maintenance = float(input('How much do you pay per year? '))
        print('Where are you located?')
        print('(1) Europe','    (2)Americas','     (3)Asia')
        i_location = int(input('Your choice?'))
    elif (imodel == '11'):
        print('CPs: ')
        print('(2)CPU', '   (3)CPU', '    (4)CPU')
        i_number_cpus = int(input('How many CPUs? '))
        i_cpu = i_number_cpus
        f_licence = i_ES40_EU
        f_maintenance = float(input('How much do you pay per year? '))
        print('Where are you located?')
        print('(1) Europe','    (2)Americas','     (3)Asia')
        i_location = int(input('Your choice?'))
    elif (imodel == '12'):
        print('CPs: ')
        print('(1) 8 CPU',' (2) 16 CPU', '   (3) 32 CPU')
        i_number_cpus = int(input('How many CPUs? '))
        i_cpu = i_number_cpus
        if i_number_cpus == '1':
            f_licence = i_GS80_EU
        elif i_number_cpus == '2':
            f_licence = i_GS160_EU
        else:
            f_licence = i_GS320_EU
        f_maintenance = float(input('How much do you pay per year? '))
        print('Where are you located?')
        print('(1) Europe','    (2)Americas','     (3)Asia')
        i_location = int(input('Your choice?'))
#elif ssystem == '2'
#elif ssystem == '3'
#else ssystem == '4'
else:
    print('Under construction')
print('the licence is',f_licence,'number of CPUs is',i_cpu)
