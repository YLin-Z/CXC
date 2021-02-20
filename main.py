from flask import Flask,render_template
from flask import request
import model #导入控制层代码

app = Flask(__name__)
# 控制层

#访问主页的路由转发
@app.route('/')
def index():
    return render_template("index.html")


# 访问东沙页面的路由转发
@app.route('/dongsha',methods=['POST','GET'])
def dongshapage():
    if request.method == 'GET':
        time = request.args.get('time')     #得到连接中的时间信息
        mapdata = model.dongsha_map(time)    #由时间得地图上的流量数据
    if request.method == 'POST':
        if request.form.get('time')=="dateandtimepoint":#当传回的时间是这个串时说明是地图右边的表单，需要日期和小时拼接成time
            time = request.form.get('date')+" "+request.form.get('timepoint')
        else:
            time = request.form.get('time')
        mapdata = model.dongsha_map(time)
    if mapdata['error']==1:
        return render_template("errorpage.html")
    else:
        return render_template("dongsha.html",data=mapdata)


# 访问南漖村页面的路由转发
@app.route('/nanjiaocun',methods=['POST','GET'])
def nanjiaocunpage():
    if request.method == 'GET':
        time = request.args.get('time')     #得到连接中的时间信息
        mapdata = model.nanjiaocun_map(time)    #由时间得地图上的流量数据
    if request.method == 'POST':
        if request.form.get('time')=="dateandtimepoint":#当传回的时间是这个串时说明是地图右边的表单，需要日期和小时拼接成time
            time = request.form.get('date')+" "+request.form.get('timepoint')
        else:
            time = request.form.get('time')
        mapdata = model.nanjiaocun_map(time)
    if mapdata['error']==1:
        return render_template("errorpage.html")
    else:
        return render_template("nanjiaocun.html",data=mapdata)


@app.route('/shaluocun',methods=['POST','GET'])
def shaluocunpage():
    if request.method == 'GET':
        time = request.args.get('time')     #得到连接中的时间信息
        mapdata = model.shaluocun_map(time)    #由时间得地图上的流量数据
    if request.method == 'POST':
        if request.form.get('time')=="dateandtimepoint":#当传回的时间是这个串时说明是地图右边的表单，需要日期和小时拼接成time
            time = request.form.get('date')+" "+request.form.get('timepoint')
        else:
            time = request.form.get('time')
        mapdata = model.shaluocun_map(time)
    if mapdata['error']==1:
        return render_template("errorpage.html")
    else:
        return render_template("shaluocun.html",data=mapdata)


# 访问西塱页面的路由转发
@app.route('/xilang',methods=['POST','GET'])
def xilangpage():
    if request.method == 'GET':
        time = request.args.get('time')     #得到连接中的时间信息
        mapdata = model.xilang_map(time)    #由时间得地图上的流量数据
    if request.method == 'POST':
        if request.form.get('time')=="dateandtimepoint":#当传回的时间是这个串时说明是地图右边的表单，需要日期和小时拼接成time
            time = request.form.get('date')+" "+request.form.get('timepoint')
        else:
            time = request.form.get('time')
        mapdata = model.xilang_map(time)
    if mapdata['error']==1:
        return render_template("errorpage.html")
    else:
        return render_template("xilang.html",data=mapdata)


if __name__ == '__main__':
    app.run(debug=True)

