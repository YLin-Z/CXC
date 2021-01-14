import getdatautils

# 得到东沙地图上的流量计数据
def dongsha_map(time):
    mapdata = getdatautils.getdongsha_shiliuliang(time)     #从EXCEL中得到时流量
    return mapdata