# def setRunningCost(spec):
#     isLoco = spec[8]
#     capacity = spec[5]
#     speed = spec[0]
#     power = spec[1]

#     if isLoco:
#         return int(pow(power*(speed-50)/5, 0.7) + 200)
#     else:
#         return int(pow(speed-70 if speed>70 else 0, 0.8)*10 + power/2 + capacity*3.5)
    
# def setPrice(spec):
#     isLoco = spec[8]
#     runningCost = spec[4]
#     speed = spec[0]
#     power = spec[1]

#     if isLoco:
#         return int(runningCost/400 + (speed-70 if speed>70 else 0)/50 + power/1000 + 1)
#     else:
#         return int(runningCost/200 + power/100 + (speed-70 if speed>70 else 0)/15 + 1)

#   출력 계산 표준공식
#   출력 ≒ 가속도 * (최고속도-50) * 무게 / 80

#   가격 계산 표준공식 (객차용)
#   가격 ≒ 출력 * 량 당 승객 * 량수 * 1000
#   유지비 ≒ 가격 / 3

def setRunningCost(spec):
    runningcost = spec[4] / 400000
    return int(runningcost)

def setPrice(spec):
    price = spec[3] / 26000000
    return int(price)

trainList = {}
#                                 0       1       2       3             4               5           6       7               8
#                                 Speed   Power   Weight  Price         Running Cost    Capacity    Doors   Introduction    isLoco
#
trainList['4400'] =               105,    1650,   88,     1700100100,   400100100,      0,          1,      (2001, 1, 1),   True
trainList['7000'] =               150,    3700,   119,    2800100100,   1500100100,     0,          1,      (1986, 1, 1),   True
trainList['7x00'] =               150,    3000,   130,    2550100100,   1290100100,     0,          1,      (1971, 1, 1),   True
trainList['7600'] =               150,    3490,   132,    2750100100,   1290100100,     0,          1,      (2014, 1, 1),   True
trainList['8000'] =               85,     5400,   132,    2440100100,   640100100,      0,          1,      (1972, 1, 1),   True
trainList['8x00'] =               150,    7000,   88,     3600100100,   1100100100,     0,          1,      (1990, 1, 1),   True
trainList['8500'] =               150,    8850,   152,    4400100100,   1300100100,     0,          1,      (2012, 1, 1),   True

trainList['DHC']                = 150,    600,    50,     1625000100,   740100100,      20,         4,      (1987, 1, 1),   False

trainList['SUX1']           =     300,    5800,   1000,   7520100100,   2450100100,     48,         4,      (2004, 1, 1),   True
trainList['SUX2']           =     300,    3200,   500,    3940100100,   1400100100,     44,         4,      (2008, 1, 1),   True
trainList['SUXK']           =     260,    2800,   300,    4200100100,   1400100100,     65,         4,      (2019, 1, 1),   True
trainList['SUX3']           =     300,    3700,   400,    6800100100,   1950100100,     65,         4,      (2024, 1, 1),   True

trainList['MWONCHUN']       =     180,    1550,   400,    1750100100,   850100100,      42,         4,      (2011, 1, 1),   False
trainList['NEWMAEUL']       =     150,    1000,   300,    1800100100,   600100100,      63,         4,      (2013, 1, 1),   False
trainList['SIMJUNG4']       =     150,    670,    200,    1400100100,   480100100,      66,         4,      (2022, 1, 1),   False
trainList['SIMJUNG6']       =     150,    1000,   300,    1800100100,   600100100,      65,         4,      (2024, 1, 1),   False
trainList['NORIRO']         =     150,    780,    200,    1480100100,   520100100,      67,         4,      (2009, 1, 1),   False

trainList['METRO']          =     90,     None,   None,   None,         None,           200,        16,     None,           False
trainList['METRO_4CAR']     =     None,   480,    200,    1500100100,   500100100,      800,        None,   None,           False
trainList['METRO_6CAR']     =     None,   720,    300,    2100100100,   700100100,      1200,       None,   None,           False
trainList['METRO_8CAR']     =     None,   960,    400,    2700100100,   900100100,      1600,       None,   None,           False
trainList['METRO_10CAR']    =     None,   1200,   500,    3300100100,   1100100100,     2000,       None,   None,           False
trainList['RTX_A']          =     180,    1500,   400,    3800100100,   2250100100,     200,        9,      (2024, 1, 1),   False
trainList['AREX_1000']      =     110,    785,    300,    2100100100,   450100100,      48,         8,      (2006, 1, 1),   False
trainList['AREX_2000_1']    =     110,    720,    300,    2600100100,   880100100,      200,        16,     (2005, 1, 1),   False
trainList['AREX_2000_4']    =     150,    960,    300,    3200100100,   1250100100,     200,        16,     (2025, 1, 1),   False

trainList['LRT']            =     70,     None,   None,   None,         None,           150,        8,      None,           False
trainList['LRT_2CAR']       =     None,   400,    60,     800100100,    250100100,      300,        None,   None,           False
trainList['LRT_4CAR']       =     None,   400,    60,     1200100100,   350100100,      600,        None,   None,           False
trainList['LRT_6CAR']       =     None,   600,    60,     1600100100,   450100100,      900,        None,   None,           False
trainList['SILLIM']         =     60,     600,    50,     600100100,    200100100,      100,        8,      (2020, 1, 1),   False

trainList['SHIN_E5']        =     321,    4200,   500,    5400100100,   2200100100,     73,         4,      (2011, 1, 1),   False
trainList['SHIN_E6']        =     321,    3600,   350,    4200100100,   1700100100,     72,         4,      (2013, 1, 1),   False
trainList['SHIN_N700_8']    =     260,    3400,   400,    4750100100,   2050100100,     68,         4,      (2005, 1, 1),   False
trainList['SHIN_N700_16']   =     300,    6200,   800,    9800100100,   3500100100,     82,         4,      (2005, 1, 1),   False
trainList['SHIN_N700S_6']   =     260,    3000,   300,    3800100100,   1650100100,     68,         4,      (2013, 1, 1),   False
trainList['SHIN_N700S_16']  =     300,    6800,   800,    10600100100,  3900100100,     82,         4,      (2013, 1, 1),   False

trainList['KSEI_AE']        =     160,    1200,   400,    3500100100,   900100100,      50,         4,      (2013, 1, 1),   False

trainList['CR400AF_8CAR']   =     350,    2800,   400,    3800100100,   1900100100,     72,         4,      (2015, 1, 1),   False
trainList['CR400AF_16CAR']  =     350,    5600,   800,    7200100100,   3400100100,     75,         4,      (2015, 1, 1),   False
trainList['CR400AF_17CAR']  =     350,    5600,   850,    7600100100,   3600100100,     75,         4,      (2015, 1, 1),   False

# wagon                           0       1       2       3              4        5             6       7
#                                 speed1  speed2  cost    running_cost   capacity loading_speed weight  introduction

trainList['SAEMAEUL_CAR']       = 150,    150,    5000,   50,            64,      10,           60,     (1969, 1, 1)
trainList['MUGUNGHWA_CAR']      = 135,    135,    5000,   50,            72,      10,           90,     (1970, 1, 1)
trainList['TONGIL_CAR']         = 120,    120,    5000,   50,            72,      10,           90,     (1963, 1, 1)
trainList['BIDULGI_CAR']        = 110,    110,    5000,   80,            100,     10,           150,    (1927, 1, 1)
trainList['GENERATOR_CAR']      = 120,    120,    100,    0,             0,       10,           50,     (1972, 1, 1)
trainList['CAFE_CAR']           = 120,    120,    5000,   30,            50,      10,           50,     (1972, 1, 1)
trainList['NARROW_GAUGE_WAGON'] = None,   None,   5000,   20,            90,      10,           30,     (1952, 1, 1)
trainList['NARROW_BOXCAR']      = None,   None,   80,     20,            12,      5,            25,     (1952, 1, 1)
trainList['NARROW_HOPPERCAR']   = None,   None,   80,     20,            12,      5,            25,     (1952, 1, 1)
trainList['FLAT_CAR']           = 120,    120,    5000,   40,            50,      5,            40,     (1950, 1, 1)
trainList['HOPPER_CAR']         = 120,    120,    5000,   40,            50,      5,            50,     (1950, 1, 1)
trainList['BAGGAGE_CAR']        = 120,    120,    5000,   40,            35,      5,            50,     (1950, 1, 1)
trainList['BOX_CAR']            = 120,    120,    5000,   40,            51,      5,            50,     (1966, 1, 1)
trainList['BOX_CAR_2003']       = 120,    120,    None,   None,          51,      None,         50,     (2003, 1, 1)
trainList['BOX_CAR_1998']       = 100,    100,    None,   None,          51,      None,         50,     (1998, 1, 1)
trainList['BOX_CAR_1996']       = 90,     90,     None,   None,          48,      None,         50,     (1996, 1, 1)
trainList['BOX_CAR_1972']       = 90,     90,     None,   None,          48,      None,         50,     (1972, 1, 1)
trainList['BOX_CAR_1966']       = 90,     90,     None,   None,          48,      None,         50,     (1966, 1, 1)
trainList['TANK_CAR']           = 120,    120,    5000,   40,            40,      5,            50,     (1950, 1, 1)
trainList['BULK_CEMENT_CAR']    = 120,    120,    5000,   40,            32,      5,            50,     (1950, 1, 1)
trainList['MAIL_CAR']           = None,   None,   5000,   40,            50,      5,            50,     (1950, 1, 1)
trainList['SUX_MAIL_CAR']       = None,   None,   5000,   220,           50,      5,            50,     (1950, 1, 1)
trainList['SLEEPING_CAR']       = None,   None,   6000,   20,            28,      5,            50,     (1966, 1, 1)
trainList['STAKE_CAR']          = 120,    120,    5000,   40,            52,      5,            50,     (1950, 1, 1)
trainList['CABOOSE']            = 120,    120,    3000,   0,             0,       5,            50,     (1999, 1, 1)
trainList['CABOOSE_BAGGAGE']    = 120,    120,    3000,   None,          0,       None,         50,     (1999, 1, 1)
trainList['CABOOSE_2AXLE']      = 120,    120,    3000,   None,          0,       None,         50,     (2000, 1, 1)
trainList['CABOOSE_BOX']        = 90,     90,     3000,   None,          0,       None,         50,     (1992, 1, 1)


content = ""
items   = ('Speed', 'Power', 'Weight',
           'Cost', 'RunningCost',
           'Capacity', 'LoadingSpeed'
           )

for _name in trainList:
    trainList[_name] = list(trainList[_name])

    if _name == "SAEMAEUL_CAR":
        items = ('speed', 'design_speed', 'cost',
                'runningcost', 'capacity', 'loadingspeed',
                'weight')

    # 기관차, 객차 돈 정상화
    if items[0] == 'Speed':
        if trainList[_name][4] != None:
            trainList[_name][4] = setRunningCost(trainList[_name])
        if trainList[_name][3] != None:
            trainList[_name][3] = setPrice(trainList[_name])

    i = 0
    for item in items:
        if trainList[_name][i] is not None:
            content += "#define var_" + _name + '_' + item.upper() + ' ' + str(trainList[_name][i]) + "\n"
        i += 1

    if trainList[_name][7] is not None:
        content += "#define var_" + _name + "_INTRODUCTION date" + str(trainList[_name][7]) + "\n"


f = open("./generated/spec.pnml", "w")
f.write(content)
f.close()