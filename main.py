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
    return render_template("dongsha.html",data=mapdata)

@app.route('/abc')
def helloworld():
    id = request.values.get("id")
    return f'''<form action ="/login">
            账号：<input name = "name" value = "{id}"><br>
            密码：<input name = "pwd">
            <input type = "submit">
            </form>
            '''

@app.route('/login')
def login():
    name = request.values.get("name")
    pwd = request.values.get("pwd")
    return f'name = {name} ,pwd = {pwd}'

if __name__ == '__main__':
    app.run(debug=True)

