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
            sll3195 = format(row.iloc[-1][4],'.2f')
            sll3194 = format(row.iloc[-1][8],'.2f')
            sll3196 = format(row.iloc[-1][14],'.2f')
            sll3198 = format(row.iloc[-1][17],'.2f')
            sll91830953 = format(row.iloc[-1][20],'.2f')
            sll69175303 = format(row.iloc[-1][25],'.2f')
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
