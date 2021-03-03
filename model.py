import getdatautils #导入数据层代码

# 得到东沙地图上的流量计数据
def dongsha_map(time):
    mapdatads = getdatautils.getdongsha_shiliuliang(time)     #从EXCEL中得到东沙各流量计时流量
    mapdatanjc = getdatautils.nanjiaocun_shiliuliang(time)     #从EXCEL中得到南漖各流量计时流量
    mapdatansl = getdatautils.shaluocun_shiliuliang(time)     #从EXCEL中得到沙洛各流量计时流量
    mapdataybycb = getdatautils.getyibanyuanchuanbiao_shiliuliang(time)     #从EXCEL中得到沙洛各流量计时流量
    if mapdatads['error']==0 and mapdatanjc['error']==0 and mapdatansl['error']==0 and mapdataybycb['error']==0:
        #如果没有查询错误就将各个地区的数据合到同一个字典变量中传回给页面
        mapdata = mapdatads.copy()
        mapdata.update(mapdatanjc)
        mapdata.update(mapdatansl)
        mapdata.update(mapdataybycb)
        #计算未统计水量
        #注意原始数据是负的要变号!!!!!!!!!!!!!!!!!
        #进入东沙的水量
        dongsha_in = mapdata['sll3198']
        #流出东沙的水量
        dongsha_out = mapdata['sll69175303']+mapdata['sll3194']-mapdata['sll3195']+mapdata['sll3196']
        #流入南漖的水量
        nanjiao_in = mapdata['sll91830729']+mapdata['sll91830730']
        #流入沙洛的水量
        shaluo_in = mapdata['sll91830456']+mapdata['sll91830454']+mapdata['sll91830455']
        #流入电排站的水量（不过东沙单独计算）
        dianpaizhan_in =mapdata['sll91830953']
        # 一般远传表的水量（不过东沙单独计算）
        yibanyuanchuanbiaosll = mapdata['yibanyuanchuanbiaosll']
        #未统计到的水量
        uncount = dongsha_in-dongsha_out-nanjiao_in-shaluo_in-yibanyuanchuanbiaosll
        #取两位小数
        uncount = format(uncount,'.2f')
        mapdata.update({'uncount':uncount,
                        'dongsha_in':dongsha_in,
                        'dongsha_out':dongsha_out,
                        'nanjiao_in':nanjiao_in,
                        'shaluo_in':shaluo_in,
                        'yibanyuanchuanbiaosll':yibanyuanchuanbiaosll,
                        'dianpaizhan_in':dianpaizhan_in})
    else:
        mapdata = {'error':1}
    return mapdata


#得到南漖村地图上的数据
def nanjiaocun_map(time):
    mapdatanjc = getdatautils.nanjiaocun_shiliuliang(time)     #从EXCEL中得到南漖各流量计时流量
    if mapdatanjc['error']==0:
        #如果没有查询错误就将各个地区的数据合到同一个字典变量中传回给页面
        mapdata = mapdatanjc
    else:
        mapdata = {'error':1}
    return mapdata


#得到沙洛村地图上的数据
def shaluocun_map(time):
    mapdatasl = getdatautils.shaluocun_shiliuliang(time)     #从EXCEL中得到沙洛各流量计时流量
    if mapdatasl['error']==0:
        #如果没有查询错误就将各个地区的数据合到同一个字典变量中传回给页面
        mapdata = mapdatasl
    else:
        mapdata = {'error':1}
    return mapdata


#得到西塱村地图上的数据
def xilang_map(time):
    mapdataxl = getdatautils.getxilang_shiliuliang(time)     #从EXCEL中得到西塱各流量计时流量
    if mapdataxl['error'] == 0:
        # 如果没有查询错误就将各个地区的数据合到同一个字典变量中传回给页面
        mapdata = mapdataxl
    else:
        mapdata = {'error': 1}
    return mapdata


#得到一般大用户远传地图上的数据
def yibanyuanchuanbiao_map(time):
    mapdataybycb = getdatautils.getyibanyuanchuanbiao_shiliuliang(time)     #从EXCEL中得到西塱各流量计时流量
    if mapdataybycb['error'] == 0:
        # 如果没有查询错误就将各个地区的数据合到同一个字典变量中传回给页面
        mapdata = mapdataybycb
    else:
        mapdata = {'error': 1}
    return mapdata


def hedong(time):
    mapdatahd = getdatautils.getyibanyuanchuanbiao_hedong(time)  # 从EXCEL中得到西塱各流量计时流量
    if mapdatahd['error'] == 0:
        # 如果没有查询错误就将各个地区的数据合到同一个字典变量中传回给页面
        mapdata = mapdatahd
    else:
        mapdata = {'error': 1}
    return mapdata