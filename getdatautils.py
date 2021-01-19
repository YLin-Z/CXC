import pandas as pd
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
            sll3195 = abs(float(format(row.iloc[-1][4],'.2f')))
            sll3194 = abs(float(format(row.iloc[-1][8],'.2f')))
            sll3196 = abs(float(format(row.iloc[-1][14],'.2f')))
            sll3198 = abs(float(format(row.iloc[-1][17],'.2f')))
            sll91830953 = abs(float(format(row.iloc[-1][20],'.2f')))
            sll69175303 = abs(float(format(row.iloc[-1][25],'.2f')))
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

def shaluocun_shiliuliang(time):
    if time == ' 0:00':  # 在右边表单那里没选好
        data = {"error": 1}
    else:
        sheet = pd.read_excel("D:/CXCDATA/shaluo_nanjiao.xls", sheet_name=0)
        row = sheet[sheet['时间'] == time]
        if row.empty == 1:
            data = {"error": 1}
        else:
            sll91830456 = abs(float(format(row.iloc[-1]["Unnamed: 3"], '.2f')))
            sll91830454 = abs(float(format(row.iloc[-1]["Unnamed: 7"], '.2f')))
            sll91830455 = abs(float(format(row.iloc[-1]["Unnamed: 11"], '.2f')))
            sunsllofshaluocun = abs(float(format(row.iloc[-1]["沙洛村时流量"], '.2f')))
            data = {'time': time,
                    'sll91830456': sll91830456,
                    'sll91830454': sll91830454,
                    'sll91830455': sll91830455,
                    'sunsllofshaluocun': sunsllofshaluocun,
                    'error': 0}
            # print(data)
            del sheet
    return data


def nanjiaocun_shiliuliang(time):
    if time == ' 0:00':  # 在右边表单那里没选好
        data = {"error": 1}
    else:
        sheet = pd.read_excel("D:/CXCDATA/shaluo_nanjiao.xls", sheet_name=1)
        row = sheet[sheet['时间'] == time]
        if row.empty == 1:
            data = {"error": 1}
        else:
            sll91830730 = abs(float(format(row.iloc[-1]["Unnamed: 2"], '.2f')))
            sll91830729 = abs(float(format(row.iloc[-1]["Unnamed: 6"], '.2f')))
            sll69983071 = abs(float(format(row.iloc[-1]["Unnamed: 10"], '.2f')))
            sunsllofnanjiaocun = abs(float(format(row.iloc[-1]["南漖村总和"], '.2f')))
            data = {'time': time,
                    'sll91830730': sll91830730,
                    'sll91830729': sll91830729,
                    'sll69983071': sll69983071,
                    'sunsllofnanjiaocun': sunsllofnanjiaocun,
                    'error': 0}
            # print(data)
            del sheet
    return data