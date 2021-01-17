import getdatautils #导入数据层代码

# 得到东沙地图上的流量计数据
def dongsha_map(time):
    mapdatads = getdatautils.getdongsha_shiliuliang(time)     #从EXCEL中得到时流量
    mapdatanjc = getdatautils.nanjiaocun_shiliuliang(time)     #从EXCEL中得到时流量
    if mapdatads['error']==0 and mapdatanjc['error']==0:
        mapdata = mapdatads.copy()
        mapdata.update(mapdatanjc)
    else:
        mapdata = {'error':1}
    return mapdata