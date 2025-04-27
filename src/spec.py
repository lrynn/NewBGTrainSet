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
#   아니면 5 * 실제 출력 / 루트최고속도

#   가격 계산 표준공식 (객차용)
#   가격 ≒ 루트(출력*최고속도) * (승객수, 기관차는 500으로 봄) * 10000
#   유지비 ≒ 가격 / 4

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
trainList['DEROI'] =              75,     2310,   135,    1880100100,   430100100,      0,          1,      (1943, 1, 1),   True
trainList['4400'] =               105,    1650,   88,     1080100100,   250100100,      0,          1,      (2001, 1, 1),   True
trainList['7000'] =               150,    3700,   119,    2400100100,   650100100,      0,          1,      (1986, 1, 1),   True
trainList['7x00'] =               150,    3000,   130,    2160100100,   470100100,      0,          1,      (1971, 1, 1),   True
trainList['7600'] =               150,    3490,   132,    2350100100,   580100100,      0,          1,      (2014, 1, 1),   True
trainList['8000'] =               85,     5300,   132,    2630100100,   440100100,      0,          1,      (1972, 1, 1),   True
trainList['8x00'] =               150,    7000,   88,     3300100100,   565100100,      0,          1,      (1998, 1, 1),   True
trainList['EUROSPRINTER'] =       220,    4500,   88,     3300100100,   565100100,      0,          1,      (1992, 1, 1),   True
trainList['8500'] =               150,    8857,   152,    3710100100,   750100100,      0,          1,      (2012, 1, 1),   True
trainList['MSB'] =                80,     482,    25,     300100100,    78000100,       0,          1,      (1999, 1, 1),   True

trainList['DHC'] =                150,    3000,   50,     1625000100,   540100100,      20,         2,      (1987, 1, 1),   False
trainList['NDC'] =                120,    600,    50,     450100100,    80100100,       64,         2,      (1984, 1, 1),   False
trainList['CDC'] =                120,    600,    50,     400100100,    75100100,       52,         2,      (1996, 1, 1),   False

trainList['SUX1']           =     300,    18177,  1000,   11900100100,  2750100100,     48,         2,      (2004, 1, 1),   True
trainList['SUX2']           =     300,    11800,  500,    5460100100,   1450100100,     44,         2,      (2008, 1, 1),   True
trainList['SUXK']           =     260,    8153,   300,    3270100100,   1200100100,     65,         2,      (2019, 1, 1),   True
trainList['SUX3']           =     300,    12230,  400,    5680100100,   1750100100,     65,         2,      (2024, 1, 1),   True

trainList['MWONCHUN']       =     180,    5438,   400,    1970100100,   550100100,      42,         2,      (2011, 1, 1),   False
trainList['NEWMAEUL']       =     150,    4078,   300,    1760100100,   600100100,      63,         2,      (2013, 1, 1),   False
trainList['SIMJUNG4']       =     150,    2719,   200,    1300100100,   480100100,      66,         2,      (2022, 1, 1),   False
trainList['SIMJUNG6']       =     150,    4078,   300,    1800100100,   600100100,      65,         2,      (2024, 1, 1),   False
trainList['NORIRO']         =     150,    2719,   200,    1340100100,   495100100,      67,         2,      (2009, 1, 1),   False

trainList['METRO']          =     90,     None,   None,   None,         None,           200,        8,      None,           False
trainList['METRO_2CAR']     =     None,   1080,   100,    1250100100,   300100100,      400,        None,   None,           False
trainList['METRO_4CAR']     =     None,   2160,   200,    1850100100,   500100100,      800,        None,   None,           False
trainList['METRO_6CAR']     =     None,   3240,   300,    2770100100,   700100100,      1200,       None,   None,           False
trainList['METRO_8CAR']     =     None,   4320,   400,    3680100100,   900100100,      1600,       None,   None,           False
trainList['METRO_10CAR']    =     None,   5400,   500,    4410100100,   1100100100,     2000,       None,   None,           False

trainList['SUIN_BUNDANG']   =     110,    3240,   300,    3430100100,   800100100,      1200,       8,      None,           False
trainList['RTX_A']          =     180,    8480,   400,    6800100100,   2250100100,     200,        4,      (2024, 1, 1),   False
trainList['AREX_1000']      =     110,    3589,   300,    1100100100,   450100100,      48,         4,      (2006, 1, 1),   False
trainList['AREX_2000_1']    =     110,    3589,   300,    2990100100,   880100100,      200,        8,      (2005, 1, 1),   False
trainList['AREX_2000_4']    =     150,    4773,   300,    4980100100,   1450100100,     200,        8,      (2025, 1, 1),   False
trainList['DAEGYEONG']      =     100,    1100,   100,    1630100100,   300100100,      200,        8,      None,           False

trainList['LRT']            =     70,     None,   None,   None,         None,           150,        4,      None,           False
trainList['LRT_2CAR']       =     None,   540,    60,     800100100,    250100100,      300,        None,   None,           False
trainList['LRT_4CAR']       =     None,   1080,   120,    1200100100,   350100100,      600,        None,   None,           False
trainList['LRT_6CAR']       =     None,   1620,   180,    1600100100,   450100100,      900,        None,   None,           False
trainList['SILLIM']         =     60,     815,    120,    600100100,    200100100,      100,        4,      (2020, 1, 1),   False

trainList['SHIN_E5']        =     321,    13440,  500,    7470100100,   2200100100,     73,         2,      (2011, 1, 1),   False
trainList['SHIN_E6']        =     321,    9408,   350,    5180100100,   1700100100,     72,         2,      (2013, 1, 1),   False
trainList['SHIN_N700_8']    =     260,    10200,  400,    5110100100,   1950100100,     68,         2,      (2005, 1, 1),   False
trainList['SHIN_N700_16']   =     300,    18600,  800,    14100100100,  3900100100,     82,         2,      (2005, 1, 1),   False
trainList['SHIN_N700S_6']   =     260,    9000,   300,    3600100100,   1550100100,     68,         2,      (2013, 1, 1),   False
trainList['SHIN_N700S_16']  =     300,    20400,  800,    15600100100,  3750100100,     82,         2,      (2013, 1, 1),   False

trainList['KSEI_AE']        =     160,    4620,   400,    1920100100,   1200100100,     50,         2,      (2013, 1, 1),   False

trainList['CR400AF_8CAR']   =     350,    8850,   400,    5590100100,   1800100100,     72,         2,      (2015, 1, 1),   False
trainList['CR400AF_16CAR']  =     350,    17700,  800,    10500100100,  3000100100,     75,         2,      (2015, 1, 1),   False
trainList['CR400AF_17CAR']  =     350,    18750,  850,    11100100100,  3200100100,     75,         2,      (2015, 1, 1),   False

trainList['TGV_DUPLEX']     =     320,    10850,  500,    5490100100,   1900100100,     64,         1,      (1995, 1, 1),   False
trainList['TGV_RESEAU_DUPLEX'] =  320,    10850,  500,    5490100100,   1900100100,     64,         1,      (2006, 1, 1),   False
trainList['TGV_DUPLEX_DASYE'] =   320,    11315,  500,    5650100100,   1950100100,     64,         1,      (2013, 1, 1),   False
trainList['TGV_2N2']        =     320,    11615,  500,    5850100100,   1800100100,     55,         1,      (2011, 1, 1),   False

# wagon                           0       1       2       3              4        5             6       7
#                                 speed1  speed2  cost    running_cost   capacity loading_speed weight  introduction

trainList['SAEMAEUL_CAR']       = 150,    150,    5000,   50,            64,      2,            64,     (1969, 1, 1)
trainList['MUGUNGHWA_CAR']      = 135,    135,    5000,   50,            72,      2,            72,     (1970, 1, 1)
trainList['TONGIL_CAR']         = 120,    120,    5000,   50,            72,      2,            72,     (1963, 1, 1)
trainList['BIDULGI_CAR']        = 110,    110,    5000,   80,            100,     4,            100,    (1927, 1, 1)
trainList['GENERATOR_CAR']      = 120,    120,    100,    0,             0,       10,           30,     (1972, 1, 1)
trainList['CAFE_CAR']           = 120,    120,    5000,   30,            50,      2,            50,     (1972, 1, 1)
trainList['NARROW_GAUGE_WAGON'] = None,   None,   5000,   20,            90,      4,            30,     (1952, 1, 1)
trainList['NARROW_BOXCAR']      = None,   None,   80,     20,            12,      5,            25,     (1952, 1, 1)
trainList['NARROW_HOPPERCAR']   = None,   None,   80,     20,            12,      5,            25,     (1952, 1, 1)
trainList['FLAT_CAR']           = 120,    120,    5000,   40,            50,      5,            40,     (1950, 1, 1)
trainList['HOPPER_CAR']         = 120,    120,    5000,   40,            50,      5,            30,     (1950, 1, 1)
trainList['BAGGAGE_CAR']        = 120,    120,    5000,   40,            35,      5,            50,     (1950, 1, 1)
trainList['BOX_CAR']            = 120,    120,    5000,   40,            51,      5,            30,     (1966, 1, 1)
trainList['BOX_CAR_2003']       = 120,    120,    None,   None,          51,      None,         30,     (2003, 1, 1)
trainList['BOX_CAR_1998']       = 100,    100,    None,   None,          51,      None,         30,     (1998, 1, 1)
trainList['BOX_CAR_1996']       = 90,     90,     None,   None,          48,      None,         30,     (1996, 1, 1)
trainList['BOX_CAR_1972']       = 90,     90,     None,   None,          48,      None,         30,     (1972, 1, 1)
trainList['BOX_CAR_1966']       = 90,     90,     None,   None,          48,      None,         30,     (1966, 1, 1)
trainList['TANK_CAR']           = 120,    120,    5000,   40,            40,      5,            30,     (1950, 1, 1)
trainList['BULK_CEMENT_CAR']    = 120,    120,    5000,   40,            32,      5,            20,     (1950, 1, 1)
trainList['MAIL_CAR']           = None,   None,   5000,   40,            50,      5,            30,     (1950, 1, 1)
trainList['SUX_MAIL_CAR']       = None,   None,   5000,   220,           50,      5,            30,     (1950, 1, 1)
trainList['SLEEPING_CAR']       = None,   None,   6000,   20,            28,      5,            30,     (1966, 1, 1)
trainList['STAKE_CAR']          = 120,    120,    5000,   40,            52,      5,            30,     (1950, 1, 1)
trainList['CABOOSE']            = 120,    120,    3000,   0,             0,       5,            30,     (1999, 1, 1)
trainList['CABOOSE_BAGGAGE']    = 120,    120,    3000,   None,          0,       None,         30,     (1999, 1, 1)
trainList['CABOOSE_2AXLE']      = 120,    120,    3000,   None,          0,       None,         30,     (2000, 1, 1)
trainList['CABOOSE_BOX']        = 90,     90,     3000,   None,          0,       None,         30,     (1992, 1, 1)


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