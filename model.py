import getdatautils #导入数据层代码

# 得到东沙地图上的流量计数据
def dongsha_map(time):
    mapdatads = getdatautils.getdongsha_shiliuliang(time)     #从EXCEL中得到东沙各流量计时流量
    mapdatanjc = getdatautils.nanjiaocun_shiliuliang(time)     #从EXCEL中得到南漖各流量计时流量
    if mapdatads['error']==0 and mapdatanjc['error']==0:
        #如果没有查询错误就将各个地区的数据合到同一个字典变量中传回给页面
        mapdata = mapdatads.copy()
        mapdata.update(mapdatanjc)
        #计算未统计水量
        #注意原始数据是负的要变号!!!!!!!!!!!!!!!!!
        uncount = mapdata['sll3198']-(mapdata['sll69175303']+mapdata['sll3194']+mapdata['sll3195'])-(mapdata['sll91830729']+mapdata['sll91830730'])
        mapdata.update({'uncount':uncount})
    else:
        mapdata = {'error':1}
    return mapdata