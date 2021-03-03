import pandas as pd
# 读东沙表格
def getdongsha_shiliuliang(time):
    if time == ' 0:00':#在右边表单那里没选好
        data = {"error":1}
    else:
        sheet = pd.read_excel("D:/CXCDATA/dongsha.xls",sheet_name = 1)
        # sheet = pd.read_csv("D:/CXCDATA/dongsha.csv",encoding='utf-8')
        row = sheet[sheet['时间']==time]
        # 时流量 = data.iloc[-1]['东沙时流量']
        if row.empty == 1:
            data = {"error":1}
        else:
            sll3195 = float(format(row.iloc[-1][4],'.2f'))
            sll3194 = float(format(row.iloc[-1][8],'.2f'))
            sll3196 = float(format(row.iloc[-1][14],'.2f'))
            sll3198 = float(format(row.iloc[-1][17],'.2f'))
            sll91830953 = float(format(row.iloc[-1][20],'.2f'))
            sll69175303 = float(format(row.iloc[-1][25],'.2f'))
            data = {'time':time,
                    'sll3195':sll3195,
                    'sll3194':sll3194,
                    'sll3196':sll3196,
                    'sll3198':sll3198,
                    'sll91830953':sll91830953,
                    'sll69175303':sll69175303,
                    'error':0}
            # print(data)
        del sheet
    return data

# 读沙洛表格
def shaluocun_shiliuliang(time):
    if time == ' 0:00':  # 在右边表单那里没选好
        data = {"error": 1}
    else:
        sheet = pd.read_excel("D:/CXCDATA/shaluo_nanjiao.xls", sheet_name=0)
        row = sheet[sheet['时间'] == time]
        if row.empty == 1:
            data = {"error": 1}
        else:
            sll91830456 = float(format(row.iloc[-1]["Unnamed: 3"], '.2f'))
            sll91830454 = float(format(row.iloc[-1]["Unnamed: 7"], '.2f'))
            sll91830455 = float(format(row.iloc[-1]["Unnamed: 13"], '.2f'))
            sunsllofshaluocun = sll91830455+sll91830456+sll91830456
            data = {'time': time,
                    'sll91830456': sll91830456,
                    'sll91830454': sll91830454,
                    'sll91830455': sll91830455,
                    'sunsllofshaluocun': sunsllofshaluocun,
                    'error': 0}
            # print(data)
        del sheet
    return data


# 读南漖表格
def nanjiaocun_shiliuliang(time):
    if time == ' 0:00':  # 在右边表单那里没选好
        data = {"error": 1}
    else:
        sheet = pd.read_excel("D:/CXCDATA/shaluo_nanjiao.xls", sheet_name=1)
        row = sheet[sheet['时间'] == time]
        if row.empty == 1:
            data = {"error": 1}
        else:
            sll91830730 = float(format(row.iloc[-1]["Unnamed: 2"], '.2f'))
            sll91830729 = float(format(row.iloc[-1]["Unnamed: 6"], '.2f'))
            sll69983071 = float(format(row.iloc[-1]["Unnamed: 10"], '.2f'))
            sunsllofnanjiaocun = float(format(row.iloc[-1]["南漖村总和"], '.2f'))
            data = {'time': time,
                    'sll91830730': sll91830730,
                    'sll91830729': sll91830729,
                    'sll69983071': sll69983071,
                    'sunsllofnanjiaocun': sunsllofnanjiaocun,
                    'error': 0}
            # print(data)
        del sheet
    return data


## 读西塱表格
def getxilang_shiliuliang(time):
    if time == ' 0:00':#在右边表单那里没选好
        data = {"error":1}
    else:
        sheet = pd.read_excel("D:/CXCDATA/xilang.xls",sheet_name = 0)
        row = sheet[sheet['时间']==time]
        # 时流量 = data.iloc[-1]['东沙时流量']
        if row.empty == 1:
            data = {"error":1}
        else:
            sll691895227334 = float(format(row.iloc[-1]["Unnamed: 3"],'.2f'))
            sll691897037300 = float(format(row.iloc[-1]["Unnamed: 6"],'.2f'))
            sll691895227336 = float(format(row.iloc[-1]["Unnamed: 9"],'.2f'))
            sll671812700107 = float(format(row.iloc[-1]["Unnamed: 12"],'.2f'))
            sll69175303 = float(format(row.iloc[-1]["Unnamed: 18"],'.2f'))
            sll3196 = float(format(row.iloc[-1]["Unnamed: 21"],'.2f'))
            data = {'time':time,
                    'sll691895227334':sll691895227334,
                    'sll691897037300':sll691897037300,
                    'sll691895227336':sll691895227336,
                    'sll671812700107':sll671812700107,
                    'sll69175303':sll69175303,
                    'sll3196':sll3196,
                    'error':0}
            # print(data)
        del sheet
    return data


#得到一般远传表的时流量和
def getyibanyuanchuanbiao_shiliuliang(time):
    if time == ' 0:00':  # 在右边表单那里没选好
        data = {"error": 1}
    else:
        sheet = pd.read_excel("D:/CXCDATA/yibanyuanchuanbiao.xls", sheet_name=0)
        row = sheet[sheet['时间'] == time]
        if row.empty == 1:
            data = {"error": 1}
        else:
            yibanyuanchuanbiaosll = float(format(row.iloc[-1]["时流量"], '.2f'))
            data = {'time': time,
                    'yibanyuanchuanbiaosll': yibanyuanchuanbiaosll,
                    'error': 0}
            # print(data)
        del sheet
    return data


def getyibanyuanchuanbiao_hedong(time):
    if time == ' 0:00':  # 在右边表单那里没选好
        data = {"error": 1}
    else:
        sheet = pd.read_excel("D:/CXCDATA/hedong.xls", sheet_name=0)
        row = sheet[sheet['时间'] == time]
        if row.empty == 1:
            data = {"error": 1}
        else:
            hedong = float(format(row.iloc[-1]["时流量"], '.2f'))
            data = {'time': time,
                    'hedong': hedong,
                    'error': 0}
            # print(data)
        del sheet
    return data